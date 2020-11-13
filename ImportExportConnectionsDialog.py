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

from qgis.PyQt.QtCore import QDir, QFile, QIODevice, QTextStream
from qgis.PyQt.QtXml import QDomDocument
from qgis.PyQt.QtGui import QCloseEvent
from qgis.PyQt.QtWidgets import QApplication, QDialog, QDialogButtonBox, QFileDialog, QMessageBox, QPushButton, QListWidgetItem
from qgis.PyQt import uic

import os

from .Connections import Connection


class ImportExportConnectionsDialog(QDialog):

    IMPORT = 1
    EXPORT = 2

    def __init__(self, parent, mode, connectionManager, filename=None):
        QDialog.__init__(self, parent)
        ui_path = os.path.join(os.path.dirname(
            __file__), 'Ui_ImportExportConnectionsDialog.ui')
        uic.loadUi(ui_path, self)
        self.parent = parent
        self.mode = mode
        self.connectionManager = connectionManager
        self.filename = filename

        # additional buttons
        pb = QPushButton(self.tr("Select all"))
        self.buttonBox.addButton(pb, QDialogButtonBox.ActionRole)
        pb.clicked.connect(self.selectAll)

        pb = QPushButton(self.tr("Clear selection"))
        self.buttonBox.addButton(pb, QDialogButtonBox.ActionRole)
        pb.clicked.connect(self.clearSelection)

        if mode == ImportExportConnectionsDialog.IMPORT:
            self.setWindowTitle(self.tr("Import Connections"))
            self.label.setText(self.tr("Select connections to import"))
            self.buttonBox.button(
                QDialogButtonBox.Ok).setText(self.tr("Import"))
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        else:
            self.setWindowTitle(self.tr("Export Connections"))
            self.buttonBox.button(
                QDialogButtonBox.Ok).setText(self.tr("Export"))
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

        if not self.populateConnections():
            QApplication.postEvent(self, QCloseEvent())

        # use OK button for starting import and export operations
        self.buttonBox.accepted.connect(self.doExportImport)

        self.listConnections.itemSelectionChanged.connect(
            self.selectionChanged)

    def populateConnections(self):
        if self.mode == ImportExportConnectionsDialog.IMPORT:
            f = QFile(self.filename)
            if not f.open(QIODevice.ReadOnly | QIODevice.Text):
                QMessageBox.warning(self.parent, self.tr("Loading Connections"),
                                    self.tr("Cannot read file {0}:\n{1}.")
                                    .format(self.filename) .format(f.errorString()))
                return False

            doc = QDomDocument()
            ret, errorStr, errorLine, errorColumn = doc.setContent(f, True)
            if not ret:
                QMessageBox.warning(self.parent, self.tr("Loading Connections"),
                                    self.tr(
                                        "Parse error at line {0}, column {1}:\n{2}")
                                    .format(errorLine)
                                    .format(errorColumn)
                                    .format(errorStr))
                return False

            root = doc.documentElement()
            if root.tagName() != "qgsElasticsearchConnections":
                QMessageBox.information(self.parent,
                                        self.tr("Loading Connections"),
                                        self.tr("The file is not a Elasticsearch connections exchange file."))
                return False
            child = root.firstChildElement()
            while not child.isNull():
                item = QListWidgetItem()
                item.setText(child.attribute("name"))
                self.listConnections.addItem(item)
                child = child.nextSiblingElement()
            self.importRoot = root

        else:
            for connectionName in self.connectionManager.connectionNames():
                item = QListWidgetItem()
                item.setText(connectionName)
                self.listConnections.addItem(item)
        return True

    def selectAll(self):
        self.listConnections.selectAll()

    def clearSelection(self):
        self.listConnections.clearSelection()

    def doExportImport(self):
        selection = self.listConnections.selectedItems()
        if len(selection) == 0:
            QMessageBox.warning(self, self.tr("Export/Import Error"),
                                self.tr("You should select at least one connection from list."))
            return

        items = [selection[i].text() for i in range(len(selection))]

        if self.mode == ImportExportConnectionsDialog.EXPORT:

            filename, _ = QFileDialog.getSaveFileName(self, self.tr("Save Connections"), QDir.homePath(),
                                                      self.tr("XML files (*.xml *.XML)"))
            if not filename:
                return

            # ensure the user never omitted the extension from the file name
            if not filename.lower().endswith(".xml"):
                filename += '.xm'

            doc = self.saveConnections(items)

            f = QFile(filename)
            if not f.open(QIODevice.WriteOnly | QIODevice.Text | QIODevice.Truncate):
                QMessageBox.warning(self, self.tr("Saving Connections"),
                                    self.tr("Cannot write file {0}:\n{1}.")
                                    .format(filename).format(f.errorString()))
                return

            out = QTextStream(f)
            doc.save(out, 4)

        else:
            self.loadConnections(items)

            # clear connections list and close window
            self.listConnections.clear()
            self.accept()

    def saveConnections(self, connectionNames):
        doc = QDomDocument("connections")
        root = doc.createElement("qgsElasticsearchConnections")
        root.setAttribute("version", "1.0")
        doc.appendChild(root)

        properties = [
            "url", "username", "password", "authcfg",
            "featureCountToEstablishFeatureDefn",
            "fidPropertyName",
            "includeJsonField",
            "flattenNestedAttributes",
            "batchSize",
            "featureIterationMaxDocs",
            "featureIterationTimeout",
            "singleRequestMaxDocs",
            "singleRequestTimeout"]

        for connectionName in connectionNames:
            conn = Connection(connectionName)
            el = doc.createElement("Elasticsearch")
            el.setAttribute("name", connectionName)
            for propName in properties:
                v = getattr(conn, propName)()
                if v is None:
                    v = ''
                elif v == True:
                    v = "true"
                elif v == False:
                    v = "false"
                else:
                    v = str(v)
                el.setAttribute(propName, v)

            root.appendChild(el)

        return doc

    def loadConnections(self, connectionNames):
        child = self.importRoot.firstChildElement()
        prompt = True
        overwrite = True

        properties = [
            "url", "username", "password", "authcfg",
            "featureCountToEstablishFeatureDefn",
            "fidPropertyName",
            "includeJsonField",
            "flattenNestedAttributes",
            "batchSize",
            "featureIterationMaxDocs",
            "featureIterationTimeout",
            "singleRequestMaxDocs",
            "singleRequestTimeout"]

        while not child.isNull():
            connectionName = child.attribute("name")
            if connectionName not in connectionNames:
                child = child.nextSiblingElement()
                continue

            # check for duplicates
            if connectionName in self.connectionManager.connectionNames() and prompt:

                res = QMessageBox.warning(self,
                                          self.tr("Loading Connections"),
                                          self.tr(
                                              "Connection with name '{0}' already exists. Overwrite?")
                                          .format(connectionName),
                                          QMessageBox.Yes | QMessageBox.YesToAll | QMessageBox.No | QMessageBox.NoToAll | QMessageBox.Cancel)

                if res == QMessageBox.Cancel:
                    return
                if res == QMessageBox.No:
                    child = child.nextSiblingElement()
                    continue
                if res == QMessageBox.Yes:
                    overwrite = True
                if res == QMessageBox.YesToAll:
                    prompt = False
                    overwrite = True
                if res == QMessageBox.NoToAll:
                    prompt = False
                    overwrite = False

            if connectionName in self.connectionManager.connectionNames() and not overwrite:
                child = child.nextSiblingElement()
                continue

            conn = Connection(connectionName)
            for propName in properties:
                getattr(
                    conn, 'set' + propName[0].upper() + propName[1:])(child.attribute(propName))
            conn.saveInSettings()

            self.connectionManager.addConnection(connectionName)

            child = child.nextSiblingElement()

    def selectionChanged(self):
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(
            len(self.listConnections.selectedItems()) != 0)
