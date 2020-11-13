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

from qgis.PyQt.QtCore import Qt, QRegExp, QSortFilterProxyModel, QUrl, QDir
from qgis.PyQt.QtGui import QStandardItemModel, QStandardItem, QDesktopServices
from qgis.PyQt.QtWidgets import (QApplication,
                                 QDialogButtonBox,
                                 QFileDialog,
                                 QMessageBox,
                                 QItemDelegate,
                                 QPushButton)
from qgis.PyQt import uic

from qgis.core import (QgsDataProvider,
                       QgsLayerItem,
                       QgsProject,
                       QgsProviderRegistry,
                       QgsVectorLayer)
from qgis.gui import QgsAbstractDataSourceWidget

from osgeo import gdal

import os

from .ConnectionDialog import ConnectionDialog
from .QueryBuilder import QueryBuilder
from .Uri import Uri

MODEL_IDX_NAME = 0
MODEL_IDX_GEOM_TYPE = 1
MODEL_IDX_SQL = 2


class ItemDelegate(QItemDelegate):

    def __init__(self, parent):
        QItemDelegate.__init__(self, parent)

    def sizeHint(self, option, index):
        size = QItemDelegate.sizeHint(self, option, index)
        size.setHeight(size.height() + 2)
        return size


class ConnectionsDialog(QgsAbstractDataSourceWidget):

    def __init__(self, parent, connectionManager):
        QgsAbstractDataSourceWidget.__init__(self, parent)
        ui_path = os.path.join(os.path.dirname(
            __file__), 'Ui_ConnectionsDialog.ui')
        uic.loadUi(ui_path, self)

        self.connectionManager = connectionManager

        self.btnNew.clicked.connect(self.btnNew_clicked)
        self.btnEdit.clicked.connect(self.btnEdit_clicked)
        self.btnDelete.clicked.connect(self.btnDelete_clicked)
        self.btnConnect.clicked.connect(self.btnConnect_clicked)
        self.lineFilter.textChanged.connect(self.filterChanged)

        self.btnLoad.clicked.connect(self.btnLoad_clicked)
        self.btnSave.clicked.connect(self.btnSave_clicked)

        self.mBuildQueryButton = QPushButton(self.tr("&Build query"))
        self.mBuildQueryButton.setToolTip(self.tr("Build query"))
        self.mBuildQueryButton.setDisabled(True)
        self.buttonBox.addButton(
            self.mBuildQueryButton, QDialogButtonBox.ActionRole)
        self.mBuildQueryButton.clicked.connect(self.buildQueryButtonClicked)

        addButton = self.buttonBox.button(QDialogButtonBox.Apply)
        addButton.setText(self.tr("&Add"))
        addButton.setToolTip(self.tr("Add selected layers to map"))
        addButton.clicked.connect(self.addButtonClicked)
        addButton.setDisabled(True)

        closeButton = self.buttonBox.button(QDialogButtonBox.Close)
        closeButton.setToolTip(
            self.tr("Close this dialog without adding any layer"))
        closeButton.clicked.connect(self.reject)

        self.buttonBox.helpRequested.connect(self.showHelp)

        self.cmbConnections.activated.connect(self.cmbConnections_activated)

        self.populateConnectionList()

        self.mModel = QStandardItemModel()
        self.mModel.setHorizontalHeaderItem(
            MODEL_IDX_NAME, QStandardItem(self.tr("Name")))
        self.mModel.setHorizontalHeaderItem(
            MODEL_IDX_GEOM_TYPE, QStandardItem(self.tr("Geometry type")))
        self.mModel.setHorizontalHeaderItem(
            MODEL_IDX_SQL, QStandardItem(self.tr("Sql or Elasticsearch JSON query")))

        self.mModelProxy = QSortFilterProxyModel(self)
        self.mModelProxy.setSourceModel(self.mModel)
        self.mModelProxy.setSortCaseSensitivity(Qt.CaseInsensitive)

        self.treeView.setModel(self.mModelProxy)
        self.treeView.setItemDelegate(
            ItemDelegate(self.treeView))
        self.treeView.doubleClicked.connect(self.treeWidgetItemDoubleClicked)
        self.treeView.selectionModel().currentRowChanged.connect(
            self.treeWidgetCurrentRowChanged)
        self.resizeTreeview()

        self.connectionManager.connectionsChanged.connect(
            self.populateConnectionList)

    def updateButtons(self):

        connections_available = self.cmbConnections.count() > 0
        # Enable/disable various buttons
        self.btnConnect.setEnabled(connections_available)
        self.btnEdit.setEnabled(connections_available)
        self.btnDelete.setEnabled(connections_available)
        self.btnSave.setEnabled(connections_available)

    def populateConnectionList(self):
        connections = self.connectionManager.connectionNames()
        self.cmbConnections.clear()
        for connection in connections:
            self.cmbConnections.addItem(connection)

        self.updateButtons()

        # set last used connection
        selectedConnection = self.connectionManager.activeConnection()
        if selectedConnection:
            index = self.cmbConnections.findText(selectedConnection)
            if index != -1:
                self.cmbConnections.setCurrentIndex(index)

    def btnNew_clicked(self):
        dlg = ConnectionDialog()
        if dlg.exec_():
            self.connectionManager.addConnection(
                self.cmbConnections.currentText())
            self.populateConnectionList()

    def btnEdit_clicked(self):
        dlg = ConnectionDialog(self.cmbConnections.currentText())
        if dlg.exec_():
            self.populateConnectionList()

    def btnDelete_clicked(self):

        msg = self.tr("Are you sure you want to remove the {0} connection and all associated settings?").format(
            self.cmbConnections.currentText())
        result = QMessageBox.question(self, self.tr(
            "Confirm Delete"), msg, QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            self.connectionManager.setActiveConnection('')
            self.connectionManager.deleteConnection(
                self.cmbConnections.currentText())
            self.updateButtons()

    def filterChanged(self, text):
        myRegExp = QRegExp(text, Qt.CaseInsensitive,
                           QRegExp.PatternSyntax(QRegExp.RegExp))
        self.mModelProxy.setFilterRegExp(myRegExp)
        self.mModelProxy.sort(self.mModelProxy.sortColumn(),
                              self.mModelProxy.sortOrder())

    def cmbConnections_activated(self, index):
        self.connectionManager.setActiveConnection(
            self.cmbConnections.currentText())
        self.btnConnect.setEnabled(True)

    def btnConnect_clicked(self):

        connectionName = self.cmbConnections.currentText()
        uri = Uri(connectionName).uri()

        self.btnConnect.setEnabled(False)
        self.mModel.removeRows(0, self.mModel.rowCount())
        QApplication.setOverrideCursor(Qt.WaitCursor)

        provider = QgsProviderRegistry.instance().createProvider(
            'ogr', uri, QgsDataProvider.ProviderOptions(), QgsDataProvider.SkipFeatureCount)
        if provider and provider.isValid():
            sublayers = provider.subLayers()
        else:
            sublayers = None

        QApplication.restoreOverrideCursor()
        self.btnConnect.setEnabled(sublayers is not None)

        if provider is None or not provider.isValid():
            QMessageBox.warning(self, self.tr("Connection Error"),
                                self.tr("Cannot connect to {0}.\nReason: {1}").format(
                                    connectionName, gdal.GetLastErrorMsg()),
                                QMessageBox.Ok)
            self.btnConnect.setEnabled(True)
            return

        for sublayer in sublayers:
            layer_idx, name, count, geom_type, geom_col_name, details = sublayer.split(
                QgsDataProvider.sublayerSeparator())

            if geom_type == 'Point':
                icon = QgsLayerItem.iconPoint()
            elif geom_type == 'LineString':
                icon = QgsLayerItem.iconLine()
            elif geom_type == 'Polygon':
                icon = QgsLayerItem.iconPolygon()
            else:
                icon = QgsLayerItem.iconTable()
            geomItem = QStandardItem(icon, geom_type)
            nameItem = QStandardItem(name)
            self.mModel.appendRow([nameItem, geomItem, QStandardItem("")])

        self.resizeTreeview()

    def resizeTreeview(self):
        self.treeView.resizeColumnToContents(MODEL_IDX_NAME)
        self.treeView.resizeColumnToContents(MODEL_IDX_GEOM_TYPE)
        self.treeView.resizeColumnToContents(MODEL_IDX_SQL)

    def addButtonClicked(self):
        # get selected entry in treeview
        currentIndex = self.treeView.selectionModel().currentIndex()
        if not currentIndex.isValid():
            return

        connectionName = self.cmbConnections.currentText()
        project = QgsProject.instance()

        # detect if a layer has several geometry types
        countOccurencesOfName = {}
        for row in range(self.mModel.rowCount()):
            layerName = self.mModel.item(row, MODEL_IDX_NAME).text()
            if layerName not in countOccurencesOfName:
                countOccurencesOfName[layerName] = 1
            else:
                countOccurencesOfName[layerName] += 1

        # create layers that user selected for this connection
        selectedRows = self.treeView.selectionModel().selectedRows()
        selectedRowsInModel = []
        for selectedRow in selectedRows:
            idx = self.mModelProxy.mapToSource(selectedRow)
            if not idx.isValid():
                continue
            row = idx.row()
            selectedRowsInModel.append(row)

        for row in selectedRowsInModel:
            layerName = self.mModel.item(row, MODEL_IDX_NAME).text()
            sql = self.mModel.item(row, MODEL_IDX_SQL).text()
            uri = Uri(connectionName).uri()+'|layername=' + layerName
            if sql:
                uri += '|subset=' + sql
            if countOccurencesOfName[layerName] > 1:
                geom_type = self.mModel.item(row, MODEL_IDX_GEOM_TYPE).text()
                uri += '|geometrytype=' + geom_type
                layerName += ' (' + geom_type + ')'
            options = QgsVectorLayer.LayerOptions(
                QgsProject.instance().transformContext())
            layer = QgsVectorLayer(uri, layerName, "ogr", options)
            project.addMapLayer(layer)

    def treeWidgetItemDoubleClicked(self, index):
        self.buildQuery(index)

    def buildQueryButtonClicked(self):
        self.buildQuery(self.treeView.selectionModel().currentIndex())

    def buildQuery(self, index):
        if not index.isValid():
            return

        row = index.row()
        layerName = index.sibling(row, MODEL_IDX_NAME).data()
        filterIndex = index.sibling(row, MODEL_IDX_SQL)
        sql = filterIndex.data()

        connectionName = self.cmbConnections.currentText()
        uri = Uri(connectionName).uri()+'|layername=' + layerName

        QApplication.setOverrideCursor(Qt.WaitCursor)
        options = QgsVectorLayer.LayerOptions(
            QgsProject.instance().transformContext())
        layer = QgsVectorLayer(uri, layerName, "ogr", options)
        QApplication.restoreOverrideCursor()
        if not layer.isValid():
            return

        # create a query builder object
        queryBuilder = QueryBuilder(layer, self)
        queryBuilder.setSql(sql)

        if queryBuilder.exec_():
            self.mModelProxy.setData(filterIndex, queryBuilder.sql())

    def treeWidgetCurrentRowChanged(self, current, previous):
        self.mBuildQueryButton.setEnabled(current.isValid())
        addButton = self.buttonBox.button(QDialogButtonBox.Apply)
        addButton.setEnabled(current.isValid())

    def showHelp(self):
        QDesktopServices.openUrl(
            QUrl("https://github.com/spatialys/QGISElasticSearchConnector"))

    def btnLoad_clicked(self):

        filename, _ = QFileDialog.getOpenFileName(self, self.tr("Load Connections"), QDir.homePath(),
                                                  self.tr("XML files (*.xml *.XML)"))
        if not filename:
            return

        from .ImportExportConnectionsDialog import ImportExportConnectionsDialog
        dlg = ImportExportConnectionsDialog(
            self, ImportExportConnectionsDialog.IMPORT, self.connectionManager, filename)
        dlg.exec_()

    def btnSave_clicked(self):
        from .ImportExportConnectionsDialog import ImportExportConnectionsDialog
        dlg = ImportExportConnectionsDialog(
            self, ImportExportConnectionsDialog.EXPORT, self.connectionManager)
        dlg.exec_()
