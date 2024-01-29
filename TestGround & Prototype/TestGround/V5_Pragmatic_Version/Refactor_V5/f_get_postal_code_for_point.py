# get_postal_code_for_point.py
from shapely.geometry import Point

def get_postal_code_for_point(latitude, longitude, postal_code_polygons):
    point = Point(longitude, latitude)

    for postal_code, polygon in postal_code_polygons.items():
        if polygon.contains(point):
            return postal_code

    return None

import json
from shapely.geometry import shape

saved_file_path = r'C:\Users\hamud\Documents\Retoflow\Project_Filter\Retoflow_Filter\Check_Out_Leon\Germany_geojson_data.geojson'

with open(saved_file_path, 'r') as file:
    geojson_data = json.load(file)

postal_code_polygons = {feature['properties']['postal_code']: shape(feature['geometry']) for feature in geojson_data['features']}

latitude = 51.316669
longitude = 9.500000
postal_code = get_postal_code_for_point(latitude, longitude, postal_code_polygons)
print(f"The postal code for the point ({latitude}, {longitude}) is: {postal_code}")
