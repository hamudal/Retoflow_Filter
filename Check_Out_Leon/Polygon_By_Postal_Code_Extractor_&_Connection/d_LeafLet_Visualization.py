import json
import geopandas as gpd
from dash import Dash, html
import dash_leaflet as dl

# Replace the file path with the actual location of your file
geojson_file_path = r"C:\Users\Admin\OneDrive\Dokumente\Projects\Retoflow_Filter-1\TestGround_&_Prototype\TestGround\Test_V7\Test_Test\Test_Dario\Polygon_By_Postal_Code_Extractor_&_Connection_V8_Test\Dash Dash Leaflet\Germany_postal_codes.geojson"

# Load GeoJSON data with geopandas
gdf = gpd.read_file(geojson_file_path)

# Extract polygons and multipolygons
polygons = gdf[gdf['geometry'].geom_type == 'Polygon']
multipolygons = gdf[gdf['geometry'].geom_type == 'MultiPolygon']

# Initialize Dash app
app = Dash(__name__)

# Define app layout
app.layout = html.Div([
    dl.Map(
        [
            dl.TileLayer(),
            # Postal code borders with polygons in blue
            dl.GeoJSON(
                data=json.loads(polygons.to_json()),
                id='polygons',
                format='geojson',
                style={'color': 'blue'}
            ),
            # Postal code borders with multipolygons in red
            dl.GeoJSON(
                data=json.loads(multipolygons.to_json()),
                id='multipolygons',
                format='geojson',
                style={'color': 'red'}
            ),
        ],
        center=[51.1657, 10.4515],  # Center of Germany
        zoom=6,
        style={'height': '50vh'},
    ),
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server()
