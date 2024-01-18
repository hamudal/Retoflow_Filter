# Retoflow_ZIP_Dict_Filter & MongoDB Connection

## Overview

This project consists of two main components:

### a_ZIP_Dict_Extractor_V2

#### GeoJson Data Approach

- **Function:** `get_place_postal_code_polygons(place_name)`
- **Description:** Fetches postal code polygons for a specified location using OSMnx.
- **Example:** `kassel_polygons = get_place_postal_code_polygons("Kassel")`

#### GeoJson Data File Kassel

- **Function:** `save_geojson_to_file(geojson_data, file_path)`
- **Description:** Saves GeoJSON data to a specified file path.
- **Example:** `save_geojson_to_file(kassel_geojson_data, 'kassel_geojson_data.geojson')`

### b_Mongo_DB_Connection_V2

#### Create MongoDB Connection

- **Function:** `create_mongo_db_connection()`
- **Description:** Creates a connection to a MongoDB instance.
- **Returns:** MongoClient instance.

#### Insert GeoJSON Data to MongoDB

- **Function:** `insert_geojson_data_to_mongo(db, collection_name, geojson_file_path)`
- **Description:** Inserts GeoJSON data into a specified MongoDB collection.

## Quick Start

1. Clone the repository.
2. Install the required dependencies.
3. Run the desired components.

## Dependencies

- Python 3.x
- OSMnx
- GeoPandas
- Matplotlib
- PyMongo

## License
