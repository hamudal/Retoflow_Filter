# b_common_functions.py
import osmnx as ox
import geojson
import pandas as pd
import os

def format_geojson_data(data):
    geojson_features = []

    for postal_code, geometry in data.items():
        if geometry.is_empty:
            continue

        coordinates = []

        if geometry.geom_type == 'Polygon':
            coordinates = [list(geometry.exterior.coords)]
        elif geometry.geom_type == 'MultiPolygon':
            coordinates = [list(poly.exterior.coords) for poly in geometry.geoms]
        else:
            raise ValueError(f"Unsupported geometry type: {geometry.geom_type}")

        feature = {
            "postal_code": postal_code,
            "geometry": {
                "type": geometry.geom_type,
                "coordinates": coordinates
            }
        }

        geojson_features.append(feature)

    return geojson.FeatureCollection(geojson_features)

def save_geojson_to_file(geojson_data, file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in locals() else os.getcwd()
    file_path = os.path.join(script_dir, file_name)

    with open(file_path, 'w') as file:
        geojson.dump(geojson_data, file, indent=2)
    return file_path
