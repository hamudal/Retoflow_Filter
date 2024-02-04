# mongodb_utils.py
import osmnx as ox
from pymongo import MongoClient
from shapely.geometry import Point, Polygon, MultiPolygon
import matplotlib.pyplot as plt

# Set the default CRS to EPSG:25832
ox.settings.default_crs = "epsg:25832"


def connect_to_mongodb(database_name, collection_name):
    """
    Connects to MongoDB and returns the MongoDB client and collection.
    """
    client = MongoClient('localhost', 27017)
    db = client[database_name]
    collection = db[collection_name]
    return client, collection


def get_polygon_from_result(result):
    """
    Retrieves Shapely Polygon or MultiPolygon from MongoDB result.
    """
    if not result.get('geometry'):
        raise UserWarning("No geometry found in the given result")

    geometry_type = result["geometry"]["type"]
    coordinates = result["geometry"]["coordinates"]

    if geometry_type == "Polygon":
        return Polygon(coordinates[0])
    elif geometry_type == "MultiPolygon":
        return MultiPolygon([Polygon(coords[0]) for coords in coordinates])
    else:
        raise UserWarning("Unsupported geometry type")


def retrieve_data_from_mongodb(collection, query):
    """
    Retrieves GeoJSON data from MongoDB collection using a geospatial query based on the specified query.
    """
    cursor = collection.find(query)
    geojson_data = {"type": "FeatureCollection", "features": list(cursor)}

    return geojson_data


def plot_polygon(polygon):
    """
    Plots a Shapely Polygon.
    """
    gdf = ox.gdf_from_geometry(polygon)
    gdf.plot()
    plt.title("Postal Code Polygon")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()
