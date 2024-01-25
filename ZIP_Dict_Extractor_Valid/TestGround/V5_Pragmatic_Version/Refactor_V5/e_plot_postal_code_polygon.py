# plot_postal_code_polygon.py
import json
from shapely.geometry import shape
import geopandas as gpd
import matplotlib.pyplot as plt

def load_geojson(file_path):
    with open(file_path, 'r') as file:
        geojson_data = json.load(file)

    postal_code_polygons = {feature['properties']['postal_code']: shape(feature['geometry']) for feature in geojson_data['features']}
    return postal_code_polygons

def plot_polygon(postal_code_polygons, postal_code):
    polygon = postal_code_polygons.get(postal_code)
    if polygon:
        gdf = gpd.GeoDataFrame(geometry=[polygon])
        gdf.plot()
        plt.title(f"Postal Code Polygon: {postal_code}")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.show()
    else:
        print(f"No polygon found for postal code: {postal_code}")

# Example usage
file_path = r'C:\Users\hamud\Documents\Retoflow\Project_Filter\Retoflow_Filter\Check_Out_Leon\Germany_geojson_data.geojson'
postal_code_polygons = load_geojson(file_path)

input_postal_code = input("Enter a postal code: ")
plot_polygon(postal_code_polygons, input_postal_code)
