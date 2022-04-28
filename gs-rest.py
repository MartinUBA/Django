# Import the library
from geo.Geoserver import Geoserver

# Initialize the library
geo = Geoserver('http://127.0.0.1:8080/geoserver', username='admin', password='geoserver')

# For creating workspace
#geo.create_workspace(workspace='demo')

# For uploading raster data to the geoserver
#geo.create_coveragestore(layer_name='Monte Hermoso', path=r'D:\Martin\GIS - PRUEBAS\Imagen satelital de Monte Hermoso\LC08_L2SP_226087_20200921_20201006_02_T1_SR_B6.tif', workspace='demo')

# For creating postGIS connection and publish postGIS table
geo.create_featurestore('postgis', workspace='demo', db='postgres', host='127.0.0.1', pg_user='postgres',pg_password='Petinato1')
geo.publish_featurestore(workspace='demo', store_name='postgis', pg_table='1900 n druid hills rd.')
