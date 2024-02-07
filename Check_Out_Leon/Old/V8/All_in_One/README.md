# GeoData Processing and MongoDB Integration

**Latest Version:** [a_Zip_Polygon_Extractor_V7.ipynb](https://github.com/hamudal/Retoflow_Filter/tree/main/Check_Out_Leon/Polygon_By_Postal_Code_Extractor_%26_Connection)

## Overview

This consolidated Jupyter Notebook (`a_Zip_Polygon_Extractor_V7.ipynb`) contains Python scripts for processing geographical data, specifically polygon shapes related to postal codes. The processed data is stored in a MongoDB database. The workflow includes:

1. Extracting and transforming polygon shapes into GeoJSON standard.
2. Saving the GeoJSON data to a file for further use.
3. Integrating the GeoJSON data into a local MongoDB database in chunks.

Additionally, there are functions to retrieve polygon shapes and data from MongoDB based on postal codes or coordinates.

## Requirements

- Python 3.x
- Required Python packages: osmnx, geopandas, shapely, pymongo, matplotlib

## Instructions

### Extract and Transform Polygon Shapes

1. Install the required packages:

    ```bash
    pip install osmnx geopandas shapely pymongo matplotlib
    ```

2. Run the script in the Jupyter Notebook (`a_Zip_Polygon_Extractor_V7.ipynb`):

    - Execute the cells related to "Extract and Transform Polygon Shapes". This fetches place polygons from OpenStreetMap, filters for valid geometries, and creates a GeoDataFrame. The resulting GeoJSON data is saved to a file, and a visualization is plotted.

### Connect to MongoDB and Integrate Data

1. Install the required packages if not already installed:

    ```bash
    pip install pymongo
    ```

2. Continue running the script in the same Jupyter Notebook (`a_Zip_Polygon_Extractor_V7.ipynb`) - the next cells:

    - Execute the cells related to "Connect to MongoDB Local, Integrate Data in Chunks". This script connects to a local MongoDB, inserts GeoJSON data in chunks, and closes the MongoDB connection.

### Polygon Functions

#### Retrieve Polygon Shape and Data

1. Continue running the script in the Jupyter Notebook (`a_Zip_Polygon_Extractor_V7.ipynb`):

    - Execute the cells related to "Poly Functions" and "Connect to MongoDB, get Polygon Shape & Data". This script connects to MongoDB, retrieves GeoJSON data, and plots the polygon for a specified postal code.

#### Find Nearest Postal Code by Coordinates

1. Continue running the script in the Jupyter Notebook (`a_Zip_Polygon_Extractor_V7.ipynb`):

    - Execute the cells related to "Poly Functions" and "Connect to MongoDB, use Coordinate and find nearest Postal Code". This script connects to MongoDB, retrieves GeoJSON data, and finds the nearest postal code based on specified coordinates. It plots the polygon for the identified postal code.

## Additional Information

- Test Polygon Data: [View on GeoJSON.io](https://geojson.io/#map=13.14/51.31281/9.48916)

---

### In-Depth

## Overview

This consolidated Jupyter Notebook (`a_Zip_Polygon_Extractor_V7.ipynb`) contains Python scripts for processing geographical data, specifically polygon shapes related to postal codes. The processed data is stored in a MongoDB database. The workflow includes:

1. **Extracting and Transforming Polygon Shapes into GeoJSON Standard:**
   - **Libraries Used:**
     - `osmnx` for fetching place polygons from OpenStreetMap.
     - `geopandas` for handling GeoDataFrames.
     - `shapely` for working with geometric objects like polygons.
     - `json` for handling GeoJSON data.
   - **Spatial Reference:**
     - The default Coordinate Reference System (CRS) is set to EPSG:25832 for consistent spatial reference (`ox.settings.default_crs = "epsg:25832"`).
   - **Handling Polygons and MultiPolygons:**
     - Place polygons fetched from OpenStreetMap are filtered for valid geometries, specifically Polygons and MultiPolygons.
     - GeoDataFrame (`gdf`) is created, containing only rows with valid geometries and associated postal codes.
     - Necessary columns (`geometry` and `postal_code`) are retained.
     - Each valid geometry is converted to GeoJSON format and stored in a list (`mongo_data_list`).
   - **Example Usage:**
     - For example, using data for "Germany" with the boundary specified as "postal_code".

2. **Saving GeoJSON Data and Visualization:**
   - GeoJSON data is saved to a file for further use (`f'{place_name}_postal_codes.geojson'`).
   - The GeoDataFrame (`gdf`) is plotted for visualization.

3. **Connecting to MongoDB and Integrating Data:**
   - **Libraries Used:**
     - `pymongo` for connecting to MongoDB.
   - **Connecting to Local MongoDB:**
     - A class (`MongoDBConnector`) is utilized to connect to a local MongoDB instance and return client and collection instances.
     - The GeoJSON data is read from the file and inserted into MongoDB in chunks.
