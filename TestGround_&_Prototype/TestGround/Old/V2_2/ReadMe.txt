# Geographical Data Extraction

## Overview a_ZIP_Dict_GeoJson_Extractor.py

This script leverages OSMnx to extract postal code polygons for a specified location. The process includes formatting the data into GeoJSON and saving it to a file.

### Functions

#### 1. `get_place_postal_code_polygons(place_name)`

- **Description:** Fetches postal code polygons using OSMnx.
- **Returns:** Dictionary with postal codes as keys and corresponding geometries.

#### 2. `format_geojson_data(data)`

- **Description:** Formats data into GeoJSON format.
- **Returns:** GeoJSON FeatureCollection.

#### 3. `save_geojson_to_file(geojson_data, file_name)`

- **Description:** Saves GeoJSON data to a file in the script's directory.
- **Returns:** File path of the saved GeoJSON.

## Quick Start

1. Run the script.
2. Input the city or country name when prompted.
3. GeoJSON data will be saved in the same directory.

## Usage

```bash
python geographical_data_extraction.py



Dependencies
OSMnx
GeoJSON
Pandas