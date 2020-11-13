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

import os

from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QApplication, QAction

from qgis.core import (QgsDataItem,
                       QgsDataCollectionItem,
                       QgsDataProvider,
                       QgsDataItemProvider,
                       QgsConnectionsRootItem,
                       QgsLayerItem,
                       QgsProviderRegistry)
from qgis.gui import QgsDataItemGuiProvider

from .Connections import ConnectionManager
from .Uri import Uri


class RootItem(QgsConnectionsRootItem):
    """ Root node for Elasticsearch connections """

    def __init__(self, parent, name, path, connectionManager):
        super().__init__(parent, name, path, "Elasticsearch")
        self.setCapabilities(self.capabilities2() | QgsDataItem.Fast)
        icon = QIcon(os.path.join(os.path.dirname(__file__),
                                  "icons", "elasticsearchconnector_icon.png"))
        self.setIcon(icon)
        self.populate()
        connectionManager.connectionsChanged.connect(self.refresh)

    def createChildren(self):
        connections = ConnectionManager().connectionNames()
        children = []
        for connectionName in connections:
            path = "es:/" + connectionName
            child = ConnectionItem(self, connectionName,
                                   path, Uri(connectionName).uri())
            children.append(child)
        return children


class ConnectionItem(QgsDataCollectionItem):
    """ Node representing a connection """

    def __init__(self, parent, name, path, uri):
        super().__init__(parent, name, path, "Elasticsearch")
        self.setCapabilities(self.capabilities2() | QgsDataItem.Collapse)
        self.uri = uri

    def createChildren(self):

        provider = QgsProviderRegistry.instance().createProvider(
            'ogr', self.uri, QgsDataProvider.ProviderOptions(), QgsDataProvider.SkipFeatureCount)
        if provider and provider.isValid():
            sublayers = provider.subLayers()
        else:
            sublayers = []

        # detect if a layer has several geometry types
        countOccurencesOfName = {}
        for sublayer in sublayers:
            layer_idx, name, count, geom_type, geom_col_name, details = sublayer.split(
                QgsDataProvider.sublayerSeparator())
            if name not in countOccurencesOfName:
                countOccurencesOfName[name] = 1
            else:
                countOccurencesOfName[name] += 1

        children = []
        for sublayer in sublayers:
            layer_idx, name, count, geom_type, geom_col_name, details = sublayer.split(
                QgsDataProvider.sublayerSeparator())
            if geom_type == 'Point':
                layerType = QgsLayerItem.Point
            elif geom_type == 'LineString':
                layerType = QgsLayerItem.Line
            elif geom_type == 'Polygon':
                layerType = QgsLayerItem.Polygon
            else:
                layerType = QgsLayerItem.Table
            uri = self.uri + '|layername=' + name
            if countOccurencesOfName[name] > 1:
                uri += '|geometrytype=' + geom_type
                name += ' (' + geom_type + ')'
            child = LayerItem(None, name, self.path() +
                              '/' + name, uri, layerType, "ogr")
            child.setState(QgsDataItem.Populated)
            children.append(child)

        return children


class LayerItem(QgsLayerItem):
    """ Node representing a layer """
    pass


class DataItemProvider(QgsDataItemProvider):
    """ Provider that creates data items nodes, starting with a RootItem """

    def __init__(self, connectionManager):
        super().__init__()
        self.connectionManager = connectionManager

    def name(self):
        return "Elasticsearch"

    def capabilities(self):
        return QgsDataProvider.Database

    def createDataItem(self, path, parent):
        return RootItem(parent, QApplication.translate("ElasticSearchConnector", "Elasticsearch"), "es:/", self.connectionManager)


class DataItemGuiProvider(QgsDataItemGuiProvider):
    """ Provider that handle GUI interactions with data items nodes """

    def __init__(self, connector):
        super().__init__()
        self.connector = connector

    def name(self):
        return "Elasticsearch"

    def populateContextMenu(self, item, menu, selectedItems, context):

        if isinstance(item, RootItem):
            action = QAction(QApplication.translate(
                "ElasticSearchConnector", "Manage connections…"), item)
            action.triggered.connect(
                self.connector.showConnectionManagerDialog)
            menu.addAction(action)

        if isinstance(item, ConnectionItem):
            action = QAction(QApplication.translate(
                "ElasticSearchConnector", "Refresh"), item)
            action.triggered.connect(item.refresh)
            menu.addAction(action)
