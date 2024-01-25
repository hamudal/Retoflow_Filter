# get_postal_code_for_polygon.py
import json
from shapely.geometry import shape

def load_geojson_from_mongo(collection):
    cursor = collection.find()
    geojson_data = {"type": "FeatureCollection", "features": []}

    for document in cursor:
        geojson_data["features"].append(document)

    return geojson_data

def get_postal_code_for_polygon(polygon, geojson_data):
    postal_code_polygons = {feature['properties']['postal_code']: shape(feature['geometry']) for feature in geojson_data['features']}

    for postal_code, geojson_polygon in postal_code_polygons.items():
        if polygon.equals(geojson_polygon
