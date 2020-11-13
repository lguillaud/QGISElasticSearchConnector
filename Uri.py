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

from .Connections import Connection


class Uri:

    def __init__(self, connectionOrConnectionName):
        if isinstance(connectionOrConnectionName, str):
            conn = Connection(connectionOrConnectionName)
        else:
            conn = connectionOrConnectionName
        url = conn.url()
        username = conn.username()
        password = conn.password()
        authcfg = conn.authcfg()

        for prefix in ('http://', 'https://'):
            if (username or password) and url.startswith(prefix):
                url = prefix + username + ':' + \
                    password + '@' + url[len(prefix):]

        self._uri = 'ES:' + url
        if authcfg:
            self._uri += " authcfg='{0}'".format(authcfg)

        v = conn.featureCountToEstablishFeatureDefn()
        if v:
            self._uri += "|option:FEATURE_COUNT_TO_ESTABLISH_FEATURE_DEFN=" + v

        v = conn.fidPropertyName()
        if v:
            self._uri += "|option:FID=" + v

        v = conn.includeJsonField()
        self._uri += "|option:JSON_FIELD=" + ("YES" if v else "NO")

        v = conn.flattenNestedAttributes()
        self._uri += "|option:FLATTEN_NESTED_ATTRIBUTES=" + \
            ("YES" if v else "NO")

        v = conn.batchSize()
        if v:
            self._uri += "|option:BATCH_SIZE=" + v

        v = conn.featureIterationMaxDocs()
        if v:
            self._uri += "|option:FEATURE_ITERATION_TERMINATE_AFTER=" + v

        v = conn.featureIterationTimeout()
        if v:
            self._uri += "|option:FEATURE_ITERATION_TIMEOUT=" + str(v)

        v = conn.singleRequestMaxDocs()
        if v:
            self._uri += "|option:SINGLE_REQUEST_TERMINATE_AFTER=" + v

        v = conn.singleRequestTimeout()
        if v:
            self._uri += "|option:SINGLE_REQUEST_TIMEOUT=" + str(v)

    def uri(self):
        return self._uri
