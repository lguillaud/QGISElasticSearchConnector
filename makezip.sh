#!/bin/sh
rm -rf tmpzip/QGISElasticSearchConnector
mkdir -p tmpzip/QGISElasticSearchConnector
cp *.py *.ui metadata.txt README.rst tmpzip/QGISElasticSearchConnector
cp -r i18n icons tmpzip/QGISElasticSearchConnector
(cd tmpzip && zip -9r ../QGISElasticSearchConnector.zip QGISElasticSearchConnector)
rm -rf tmpzip
