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

from qgis.PyQt.QtCore import QObject
from qgis.PyQt.QtCore import pyqtSignal

from qgis.core import QgsOwsConnection, QgsSettings

# Used to store Elastisearch connections in QgsSettings (under 'qgis/connections-' + CONNECTION_KEY)
CONNECTION_KEY = 'elasticsearch'


class ConnectionManager(QObject):
    """ This class manages the list of connections """

    connectionsChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def connectionNames(self):
        return QgsOwsConnection.connectionList(CONNECTION_KEY)

    def addConnection(self, name):
        self.connectionsChanged.emit()

    def deleteConnection(self, name):
        QgsOwsConnection.deleteConnection(CONNECTION_KEY, name)
        Connection(name).clearSettings()
        self.connectionsChanged.emit()

    def setActiveConnection(self, name):
        QgsOwsConnection.setSelectedConnection(CONNECTION_KEY, name)

    def activeConnection(self):
        return QgsOwsConnection.selectedConnection(CONNECTION_KEY)


class Connection:
    """ This class manages the settings of a connection """

    def __init__(self, connectionName=None):
        self.mUrl = None
        self.mUsername = None
        self.mPassword = None
        self.mAuthcfg = None
        self.mFeatureCountToEstablishFeatureDefn = None
        self.mFidPropertyName = None
        self.mIncludeJsonField = False
        self.mFlattenNestedAttributes = True
        self.mBatchSize = None
        self.mFeatureIterationMaxDocs = None
        self.mFeatureIterationTimeout = None
        self.mSingleRequestMaxDocs = None
        self.mSingleRequestTimeout = None
        self.connectionName = connectionName
        if connectionName:
            self.key = 'qgis/connections-' + CONNECTION_KEY + '/' + connectionName
            self.loadFromSettings()

    @staticmethod
    def _castToBool(v):
        # For some reason, QgsSettings() return a string, and not a boolean
        if v == 'true':
            return True
        elif v == 'false':
            return False
        return v

    def loadFromSettings(self):
        settings = QgsSettings()
        self.mUrl = settings.value(self.key + "/url")
        self.mUsername = settings.value(self.key + "/username")
        self.mPassword = settings.value(self.key + "/password")
        self.mAuthcfg = settings.value(self.key + "/authcfg")
        self.mFeatureCountToEstablishFeatureDefn = settings.value(
            self.key + "/featureCountToEstablishFeatureDefn")
        self.mFidPropertyName = settings.value(self.key + "/fidPropertyName")
        self.mIncludeJsonField = Connection._castToBool(settings.value(
            self.key + "/includeJsonField", False))
        self.mFlattenNestedAttributes = Connection._castToBool(settings.value(
            self.key + "/flattenNestedAttributes", True))
        self.mBatchSize = settings.value(self.key + "/batchSize")
        self.mFeatureIterationMaxDocs = settings.value(
            self.key + "/featureIterationMaxDocs")
        self.mFeatureIterationTimeout = settings.value(
            self.key + "/featureIterationTimeout")
        self.mSingleRequestMaxDocs = settings.value(
            self.key + "/singleRequestMaxDocs")
        self.mSingleRequestTimeout = settings.value(
            self.key + "/singleRequestTimeout")

    def saveInSettings(self):
        settings = QgsSettings()
        settings.setValue(self.key + "/url", self.mUrl)
        settings.setValue(self.key + "/username", self.mUsername)
        settings.setValue(self.key + "/password", self.mPassword)
        settings.setValue(self.key + "/authcfg", self.mAuthcfg)
        settings.setValue(self.key + "/featureCountToEstablishFeatureDefn",
                          self.mFeatureCountToEstablishFeatureDefn)
        settings.setValue(self.key + "/fidPropertyName", self.mFidPropertyName)
        settings.setValue(self.key + "/includeJsonField",
                          self.mIncludeJsonField)
        settings.setValue(self.key + "/flattenNestedAttributes",
                          self.mFlattenNestedAttributes)
        settings.setValue(self.key + "/batchSize", self.mBatchSize)
        settings.setValue(self.key + "/featureIterationMaxDocs",
                          self.mFeatureIterationMaxDocs)
        settings.setValue(self.key + "/featureIterationTimeout",
                          self.mFeatureIterationTimeout)
        settings.setValue(self.key + "/singleRequestMaxDocs",
                          self.mSingleRequestMaxDocs)
        settings.setValue(self.key + "/singleRequestTimeout",
                          self.mSingleRequestTimeout)

    def clearSettings(self):
        settings = QgsSettings()
        settings.remove(self.key)
        settings.sync()

    def url(self):
        return self.mUrl

    def username(self):
        return self.mUsername

    def password(self):
        return self.mPassword

    def authcfg(self):
        return self.mAuthcfg

    def featureCountToEstablishFeatureDefn(self):
        return self.mFeatureCountToEstablishFeatureDefn

    def fidPropertyName(self):
        return self.mFidPropertyName

    def includeJsonField(self):
        return self.mIncludeJsonField

    def flattenNestedAttributes(self):
        return self.mFlattenNestedAttributes

    def batchSize(self):
        return self.mBatchSize

    def featureIterationMaxDocs(self):
        return self.mFeatureIterationMaxDocs

    def featureIterationTimeout(self):
        return self.mFeatureIterationTimeout

    def singleRequestMaxDocs(self):
        return self.mSingleRequestMaxDocs

    def singleRequestTimeout(self):
        return self.mSingleRequestTimeout

    def setUrl(self, url):
        self.mUrl = url

    def setUsername(self, username):
        self.mUsername = username

    def setPassword(self, password):
        self.mPassword = password

    def setAuthcfg(self, authcfg):
        self.mAuthcfg = authcfg

    def setFeatureCountToEstablishFeatureDefn(self, featureCountToEstablishFeatureDefn):
        self.mFeatureCountToEstablishFeatureDefn = featureCountToEstablishFeatureDefn

    def setFidPropertyName(self, fidPropertyName):
        self.mFidPropertyName = fidPropertyName

    def setIncludeJsonField(self, includeJsonField):
        self.mIncludeJsonField = Connection._castToBool(includeJsonField)

    def setFlattenNestedAttributes(self, flattenNestedAttributes):
        self.mFlattenNestedAttributes = Connection._castToBool(
            flattenNestedAttributes)

    def setBatchSize(self, batchSize):
        self.mBatchSize = batchSize

    def setFeatureIterationMaxDocs(self, featureIterationMaxDocs):
        self.mFeatureIterationMaxDocs = featureIterationMaxDocs

    def setFeatureIterationTimeout(self, featureIterationTimeout):
        self.mFeatureIterationTimeout = float(
            featureIterationTimeout) if featureIterationTimeout else None

    def setSingleRequestMaxDocs(self, singleRequestMaxDocs):
        self.mSingleRequestMaxDocs = singleRequestMaxDocs

    def setSingleRequestTimeout(self, singleRequestTimeout):
        self.mSingleRequestTimeout = float(
            singleRequestTimeout) if singleRequestTimeout else None
