# -*- coding: utf-8 -*-
"""
***************************************************************************
Name                 : ElasticSearchConnector
Description          : ElasticSearchConnector
Date                 : 05/Oct/2020
copyright            : (C) Even Rouault 2020
email                : even.rouault@spatialys.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from qgis.PyQt.QtCore import Qt, QUrl
from qgis.PyQt.QtGui import QDesktopServices
from qgis.PyQt.QtWidgets import QApplication, QDialog, QDialogButtonBox, QMessageBox
from qgis.PyQt import uic

from qgis.core import QgsDataProvider, QgsProviderRegistry

from osgeo import gdal

import os

from .Connections import ConnectionManager, Connection
from .Uri import Uri


class ConnectionDialog(QDialog):
    def __init__(self, originalConnName=""):
        QDialog.__init__(self)
        ui_path = os.path.join(os.path.dirname(
            __file__), 'Ui_ConnectionDialog.ui')
        uic.loadUi(ui_path, self)

        if originalConnName:
            self.setWindowTitle(self.tr("Modify Connection"))

        self.originalConnName = originalConnName

        okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        okButton.setDisabled(True)
        self.txtName.textChanged.connect(self.updateOkButtonState)
        self.txtUrl.textChanged.connect(self.updateOkButtonState)

        self.buttonBox.helpRequested.connect(self.showHelp)

        self.mTestConnectionButton.clicked.connect(self.testConnection)

        if originalConnName:
            # populate the dialog with the information stored for the connection
            self._setWidgetsFromConnection(originalConnName)

        self.spinFeatureIterationTimeout.setShowClearButton(True)
        self.spinFeatureIterationTimeout.setSpecialValueText(self.tr('none'))
        self.spinFeatureIterationTimeoutSingleRequest.setShowClearButton(True)
        self.spinFeatureIterationTimeoutSingleRequest.setSpecialValueText(
            self.tr('none'))

    def updateOkButtonState(self):
        enabled = self.txtName.text() != '' and self.txtUrl.text() != ''
        okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        okButton.setEnabled(enabled)

    def validate(self):

        # warn if entry was renamed to an existing connection
        if (self.originalConnName == '' or self.originalConnName != self.txtName.text()) and self.txtName in ConnectionManager().connectionNames():
            if QMessageBox.question(self,
                                    self.tr("Save Connection"),
                                    self.tr("Should the existing connection {0} be overwritten?").format(
                                        self.txtName.text()),
                                    QMessageBox.Ok | QMessageBox.Cancel) == QMessageBox.Cancel:
                return False

        if self.mAuthSettings.password():
            if QMessageBox.question(self,
                                    self.tr("Saving Passwords"),
                                    self.tr("WARNING: You have entered a password. It will be stored in unsecured plain text in your project files and your home directory (Unix-like OS) or user profile (Windows). If you want to avoid this, press Cancel and either:\n\na) Don't provide a password in the connection settings — it will be requested interactively when needed;\nb) Use the Configuration tab to add your credentials in an HTTP Basic Authentication method and store them in an encrypted database."),
                                    QMessageBox.Ok | QMessageBox.Cancel) == QMessageBox.Cancel:
                return False

        return True

    def _setWidgetsFromConnection(self, connectionName):
        self.txtName.setText(connectionName)
        connection = Connection(connectionName)
        self.txtUrl.setText(connection.url())
        self.mAuthSettings.setUsername(connection.username())
        self.mAuthSettings.setPassword(connection.password())
        self.mAuthSettings.setConfigId(connection.authcfg())
        self.txtMaxNumFeaturesFeatureDefn.setText(
            connection.featureCountToEstablishFeatureDefn())
        self.txtFIDColumnName.setText(connection.fidPropertyName())
        self.cbxIncludeJSON.setChecked(connection.includeJsonField())
        self.cbxFlattenNestedAttributes.setChecked(
            connection.flattenNestedAttributes())
        self.txtBatchSize.setText(connection.batchSize())
        self.txtMaxDocumentCount.setText(connection.featureIterationMaxDocs())
        v = connection.featureIterationTimeout()
        if v:
            self.spinFeatureIterationTimeout.setValue(float(v))
        else:
            self.spinFeatureIterationTimeout.cleanText()
        self.txtMaxDocumentCountSingleRequest.setText(
            connection.singleRequestMaxDocs())
        v = connection.singleRequestTimeout()
        if v:
            self.spinFeatureIterationTimeoutSingleRequest.setValue(float(v))
        else:
            self.spinFeatureIterationTimeoutSingleRequest.cleanText()

    def _createConnectionFromWidgets(self, connectionName=None):
        connection = Connection(connectionName)
        connection.setUrl(self.txtUrl.text().strip())
        connection.setUsername(self.mAuthSettings.username())
        connection.setPassword(self.mAuthSettings.password())
        connection.setAuthcfg(self.mAuthSettings.configId())
        connection.setFeatureCountToEstablishFeatureDefn(
            self.txtMaxNumFeaturesFeatureDefn.text())
        connection.setFidPropertyName(self.txtFIDColumnName.text())
        connection.setIncludeJsonField(self.cbxIncludeJSON.isChecked())
        connection.setFlattenNestedAttributes(
            self.cbxFlattenNestedAttributes.isChecked())
        connection.setBatchSize(self.txtBatchSize.text())
        connection.setFeatureIterationMaxDocs(self.txtMaxDocumentCount.text())
        v = self.spinFeatureIterationTimeout.value()
        connection.setFeatureIterationTimeout(v if v != 0 else None)
        connection.setSingleRequestMaxDocs(
            self.txtMaxDocumentCountSingleRequest.text())
        v = self.spinFeatureIterationTimeoutSingleRequest.value()
        connection.setSingleRequestTimeout(v if v != 0 else None)
        return connection

    def accept(self):

        if not self.validate():
            return

        # on rename, delete original entry first
        connectionName = self.txtName.text()
        if self.originalConnName != '' and self.originalConnName != connectionName:
            Connection(self.originalConnName).clearSettings()

        self._createConnectionFromWidgets(connectionName).saveInSettings()

        ConnectionManager().setActiveConnection(connectionName)

        return QDialog.accept(self)

    def testConnection(self):
        uri = Uri(self._createConnectionFromWidgets()).uri()

        QApplication.setOverrideCursor(Qt.WaitCursor)
        provider = QgsProviderRegistry.instance().createProvider(
            'ogr', uri, QgsDataProvider.ProviderOptions(), QgsDataProvider.SkipFeatureCount)
        ok = provider and provider.isValid()
        QApplication.restoreOverrideCursor()

        url = self.txtUrl.text().strip()
        if ok:
            QMessageBox.information(self,
                                    self.tr("Test connection"),
                                    self.tr("Connection to {0} was successful").format(url))
        else:
            QMessageBox.warning(self, self.tr("Test connection"),
                                self.tr("Cannot connect to {0}.\nReason: {1}").format(
                                    url, gdal.GetLastErrorMsg()),
                                QMessageBox.Ok)

    def showHelp(self):
        QDesktopServices.openUrl(
            QUrl("https://github.com/spatialys/QGISElasticSearchConnector"))
