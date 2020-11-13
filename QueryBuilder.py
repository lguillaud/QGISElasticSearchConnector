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

from qgis.PyQt.QtWidgets import (QApplication,
                                 QDialog,
                                 QMessageBox)
from qgis.gui import QgsQueryBuilder

from osgeo import gdal

import json


class QueryBuilder(QgsQueryBuilder):

    def __init__(self, layer, parent):
        QgsQueryBuilder.__init__(self, layer, parent)
        self.layer = layer

        self.mOrigSubsetString = layer.subsetString()
        self.codeEditorWidget().setToolTip(
            self.tr("Enter SQL request or ElasticSearch query (JSON)"))

    def baseTranslate(self, *args):
        return QApplication.translate("QgsQueryBuilder", *args)

    def test(self):

        gdal.ErrorReset()

        if self.layer.setSubsetString(self.sql()):
            featureCount = self.layer.featureCount()

            # When using an ElasticSearch JSON filter, errors are found only
            # when reading features or issuing featureCount()
            if gdal.GetLastErrorMsg():
                self.layer.setSubsetString(None)
                msg = gdal.GetLastErrorMsg()
                try:
                    j = json.loads(msg)
                    msg = json.dumps(j, indent=4)
                except:
                    pass
                QMessageBox.warning(self,
                                    QApplication.translate(
                                        "QgsQueryBuilder",   "Query Result"),
                                    QApplication.translate(
                                        "QgsQueryBuilder",   "An error occurred when executing the query.")
                                    + QApplication.translate("QgsQueryBuilder",  "\nThe data provider said:\n%1").replace('%1', '{0}').format(msg))
                return

            # Check for errors
            if featureCount < 0:
                QMessageBox.warning(self,
                                    QApplication.translate(
                                        "QgsQueryBuilder", "Query Result"),
                                    QApplication.translate("QgsQueryBuilder", "An error occurred when executing the query, please check the expression syntax."))
            else:
                QMessageBox.information(self,
                                        QApplication.translate(
                                            "QgsQueryBuilder",  "Query Result"),
                                        QApplication.translate("QgsQueryBuilder", "The where clause returned %n row(s).", "returned test rows", featureCount))
        elif self.layer.dataProvider().hasErrors():
            QMessageBox.warning(self,
                                QApplication.translate(
                                    "QgsQueryBuilder",   "Query Result"),
                                QApplication.translate(
                                    "QgsQueryBuilder",   "An error occurred when executing the query.")
                                + QApplication.translate("QgsQueryBuilder",  "\nThe data provider said:\n%1").replace('%1', '{0}').format('\n'.join(self.layer.dataProvider().errors())))
            self.layer.dataProvider().clearErrors()
        else:
            QMessageBox.warning(self,
                                QApplication.translate(
                                    "QgsQueryBuilder", "Query Result"),
                                QApplication.translate("QgsQueryBuilder", "An error occurred when executing the query."))

    def accept(self):

        if self.sql() != self.mOrigSubsetString:
            if not self.layer.setSubsetString(self.sql()):
                # error in query - show the problem
                if self.layer.dataProvider().hasErrors():
                    QMessageBox.warning(self,
                                        self.baseTranslate("Query Result"),
                                        self.baseTranslate(
                                            "An error occurred when executing the query.")
                                        + self.baseTranslate("\nThe data provider said:\n%1").replace('%1', '{0}').format('\n'.join(self.layer.dataProvider().errors())))
                    self.layer.dataProvider().clearErrors()
                else:
                    QMessageBox.warning(self, self.baseTranslate("Query Result"), self.baseTranslate(
                        "Error in query. The subset string could not be set."))
                return

        QDialog.accept(self)
