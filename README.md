# Project Readme

## Overview

This project utilizes OSMnx, GeoPandas, Shapely, Matplotlib, and MongoDB to extract, process, and visualize postal code polygon data. It consists of two main components:

1. **a_Zip_Polygon_Dict_Extraction_V3.ipynb:** A Jupyter Notebook to extract postal code polygons from OpenStreetMap using OSMnx, convert them to GeoJSON format, and optionally save them to MongoDB.

2. **b_MongoDB_Connection_V3.ipynb:** A Jupyter Notebook containing a class that facilitates connecting to a MongoDB database, inserting GeoJSON data into a specified collection, and closing the database connection.

## Installation

1. **Dependencies:**
   - Install required Python libraries using pip:
     ```bash
     pip install osmnx geopandas matplotlib shapely pymongo
     ```

2. **MongoDB:**
   - Make sure MongoDB is installed on your local machine or update the connection details in `b_MongoDB_Connection_V3.ipynb` to point to your MongoDB server.

3. **Usage:**
   - Run `a_Zip_Polygon_Dict_Extraction_V3.ipynb` to extract postal code polygons, convert them to GeoJSON, and optionally save them to MongoDB.
   - Customize the parameters in the notebook, such as the place name, saved GeoJSON file, and MongoDB connection details.

## a_Zip_Polygon_Dict_Extraction_V3.ipynb

### Functions

#### `handle_multipolygon(multipolygon) -> List[Polygon]`
Handles the conversion of MultiPolygon or Polygon geometries to a list of Shapely Polygon objects.

#### `postal_code_polygon_dict_extractor(place_name, save_geojson=False) -> Dict[str, List[Polygon]]`
Extracts postal code polygons using OSMnx, converts them to Shapely Polygons, and optionally saves the GeoJSON file.

- **Parameters:**
  - `place_name`: The location for which postal code polygons are extracted.
  - `save_geojson`: If `True`, saves the GeoJSON file. Default is `False`.

- **Returns:**
  - A dictionary where keys are postal codes, and values are lists of Shapely Polygons representing the postal code boundaries.

#### `plot_all_postal_code_polygons(gdf, highlight_postal_code=None, zoom_into_city=False)`
Plots the GeoDataFrame containing postal code polygons on a map and optionally highlights a specific postal code.

- **Parameters:**
  - `gdf`: GeoDataFrame containing postal code polygons.
  - `highlight_postal_code`: Postal code to highlight. Default is `None`.
  - `zoom_into_city`: If `True`, zooms into the city area. Default is `False`.

## b_MongoDB_Connection_V3.ipynb

### Class: MongoDBConnector

#### `__init__(self, database_name, collection_name)`
Constructor that initializes a MongoDBConnector instance.

- **Parameters:**
  - `database_name`: Name of the MongoDB database.
  - `collection_name`: Name of the MongoDB collection.

#### `connect_to_local_mongodb(self) -> Tuple[MongoClient, Collection]`
Connects to the local MongoDB server and returns the MongoClient and Collection objects.

- **Returns:**
  - A tuple containing the MongoClient and Collection objects.

#### `insert_geojson_data(self, geojson_file_path, chunk_size=1000)`
Inserts GeoJSON data into the MongoDB collection in chunks.

- **Parameters:**
  - `geojson_file_path`: Path to the GeoJSON file.
  - `chunk_size`: Size of each insertion chunk. Default is `1000`.

#### `close_connection(self)`
Closes the MongoDB connection.

## Example Usage

### a_Zip_Polygon_Dict_Extraction_V3.ipynb

```python
# Example usage for Germany with saving GeoJSON data, using EPSG:25832,
# and optionally zooming into Kassel and highlighting a postal code
place_postal_code_polygons_germany = postal_code_polygon_dict_extractor("Germany", save_geojson=True)
highlight_postal_code_germany = "34117"
gdf_germany = gpd.GeoDataFrame(geometry=[geometry for geometries in place_postal_code_polygons_germany.values() for geometry in geometries])
gdf_germany['postal_code'] = [postal_code for postal_code in place_postal_code_polygons_germany.keys() for _ in place_postal_code_polygons_germany[postal_code]]
zoom_into_city = True
highlight_postal_code_kassel = "34117"

# Plot Germany map with highlighted postal code
plot_all_postal_code_polygons(gdf_germany, highlight_postal_code=highlight_postal_code_germany, zoom_into_city=zoom_into_city)

# Optionally, you can zoom into Kassel and highlight a postal code
if zoom_into_city:
    place_postal_code_polygons_kassel = postal_code_polygon_dict_extractor("Kassel")
    gdf_kassel = gpd.GeoDataFrame(geometry=[geometry for geometries in place_postal_code_polygons_kassel.values() for geometry in geometries])
    gdf_kassel['postal_code'] = [postal_code for postal_code in place_postal_code_polygons_kassel.keys() for _ in place_postal_code_polygons_kassel[postal_code]]

    # Plot Kassel map with highlighted postal code
    plot_all_postal_code_polygons(gdf_kassel, highlight_postal_code=highlight_postal_code_kassel)


# Example usage of the class
if __name__ == "__main__":
    # User input for the database and collection names
    database_name = "ZIP_Poly_Ger_Test"
    collection_name = "ZIP_Poly_Ger_Collection_Test"

    # Create an instance of MongoDBConnector
    mongo_connector = MongoDBConnector(database_name, collection_name)

    # Connect to MongoDB
    mongo_client, mongo_collection = mongo_connector.connect_to_local_mongodb()

    # Example GeoJSON file path
    geojson_file_path = 'Germany_postal_codes.geojson'  # Update the file path accordingly

    # Insert GeoJSON data into MongoDB
    mongo_connector.insert_geojson_data(geojson_file_path, chunk_size=1000)

    # Close MongoDB connection when done
    mongo_connector.close_connection()

