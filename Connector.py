# -*- coding: utf-8 -*-
"""
/***************************************************************************
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

from qgis.PyQt.QtCore import (QSettings, QTranslator, QCoreApplication)
from qgis.PyQt.QtGui import (QIcon)
from qgis.PyQt.QtWidgets import (QAction)

import os

from qgis.core import QgsApplication
from qgis.gui import QgsGui, QgsSourceSelectProvider, QgsSubsetStringEditorProvider

from .Connections import ConnectionManager
from .DataItems import DataItemProvider, DataItemGuiProvider


class Connector:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

        self.plugin_dir = os.path.dirname(__file__)

        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, "i18n",
                                  "ElasticSearchConnector_{}.qm".format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            assert self.translator.load(localePath)
            QCoreApplication.installTranslator(self.translator)

        self.dlg = None
        self.trName = QCoreApplication.translate(
            'ElasticSearchConnector', "Elasticsearch Connector")

    def initGui(self):

        icon = QIcon(os.path.join(self.plugin_dir, "icons",
                                  "elasticsearchconnector_icon.png"))
        self.action = QAction(icon, QCoreApplication.translate('ElasticSearchConnector',
                                                               "&Elasticsearch Connector"), self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.showConnectionManagerDialog)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        #self.iface.addPluginToVectorMenu(self.trName, self.action)

        self.actionAddLayer = QAction(icon, QCoreApplication.translate('ElasticSearchConnector',
                                                                       "Add &Elasticsearch Layer..."), self.iface.mainWindow())
        self.actionAddLayer.triggered.connect(self.showConnectionManagerDialog)
        self.iface.addLayerMenu().addAction(self.actionAddLayer)

        self.connectionManager = ConnectionManager()

        self.dataItemProvider = DataItemProvider(self.connectionManager)
        QgsApplication.dataItemProviderRegistry().addProvider(self.dataItemProvider)

        self.dataItemGuiProvider = DataItemGuiProvider(self)
        QgsGui.instance().dataItemGuiProviderRegistry().addProvider(self.dataItemGuiProvider)

        self.sourceSelectProvider = SourceSelectProvider(
            QCoreApplication.translate('ElasticSearchConnector', 'Elasticsearch'), icon, self.connectionManager)
        QgsGui.sourceSelectProviderRegistry().addProvider(self.sourceSelectProvider)

        self.subsetStringEditorProvider = SubsetStringEditorProvider()
        QgsGui.subsetStringEditorProviderRegistry().addProvider(
            self.subsetStringEditorProvider)

    def unload(self):

        # Remove the plugin menu item and icon
        #self.iface.removePluginVectorMenu(self.trName, self.action)
        self.iface.removeToolBarIcon(self.action)

        self.iface.addLayerMenu().removeAction(self.actionAddLayer)

        QgsApplication.dataItemProviderRegistry().removeProvider(self.dataItemProvider)

        QgsGui.instance().dataItemGuiProviderRegistry(
        ).removeProvider(self.dataItemGuiProvider)

        QgsGui.sourceSelectProviderRegistry().removeProvider(self.sourceSelectProvider)

        QgsGui.subsetStringEditorProviderRegistry().removeProvider(
            self.subsetStringEditorProvider)

    def showConnectionManagerDialog(self):
        if self.dlg:
            self.dlg.setFocus()
            return

        from .ConnectionsDialog import ConnectionsDialog
        self.dlg = ConnectionsDialog(
            self.iface.mainWindow(), self.connectionManager)
        self.dlg.show()
        self.dlg.adjustSize()
        self.dlg.exec_()
        self.dlg = None


class SourceSelectProvider(QgsSourceSelectProvider):

    def __init__(self, trName, icon, connectionManager):
        QgsSourceSelectProvider.__init__(self)
        self.trName = trName
        self.icon_ = icon
        self.connectionManager = connectionManager

    def providerKey(self):
        return "Elasticsearch"

    def text(self):
        return self.trName

    def icon(self):
        return self.icon_

    def createDataSourceWidget(self, parent, flags, widgetMode):
        from .ConnectionsDialog import ConnectionsDialog
        return ConnectionsDialog(parent, self.connectionManager)


class SubsetStringEditorProvider(QgsSubsetStringEditorProvider):

    def providerKey(self):
        return "Elasticsearch"

    def canHandleLayer(self, layer):
        return layer.dataProvider().name() == 'ogr' and self.canHandleLayerStorageType(layer)

    def canHandleLayerStorageType(self, layer):
        return layer.dataProvider().storageType() == 'Elasticsearch'

    def createDialog(self, layer, parent, flags):
        from .QueryBuilder import QueryBuilder
        return QueryBuilder(layer, parent)
