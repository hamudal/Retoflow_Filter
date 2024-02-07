# Geographic Data Processing README

This README provides an overview of three Python scripts designed for geographic data processing. Each script serves a specific function within the context of handling geographic information.

## Script 1: a_Polygon_By_Postal_Code_Extractor_V8.ipynb

### Purpose
This script is responsible for fetching postal code polygons based on a specified location, filtering and processing the retrieved data, and finally saving it in GeoJSON format.

### Dependencies
- osmnx
- geopandas
- shapely

### Usage
```python
result_data = fetch_and_save_postal_codes(place_name="Germany", tags={"boundary": "postal_code"}, save_file=True)
```

## Script 2: b_MongoDB_Connection.ipynb

### Purpose
The purpose of this script is to establish a connection with a MongoDB database, insert GeoJSON data into it, create a 2D spatial index, and then close the connection.

### Dependencies
- pymongo
- json

### Configuration
The script retrieves connection parameters from a `config.json` file.

### Usage
```bash
python b_MongoDB_Connection.ipynb
```

## Script 3: c_Exploration_Tools.ipynb

### Purpose
This script facilitates querying a MongoDB collection to retrieve the polygon corresponding to a specific postal code, along with its geometry.

### Dependencies
- osmnx
- pymongo
- shapely
- json

### Configuration
The MongoDB connection details and the path to the GeoJSON file are specified within the script.

### Usage
```python
python c_Exploration_Tools.ipynb
```

Feel free to copy this Markdown-formatted README and use it in your project documentation.
