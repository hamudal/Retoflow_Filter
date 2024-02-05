import geopandas as gpd
from dash import Dash, dcc, html
import dash_leaflet as dl

# Replace the file path with the actual location of your file
geojson_file_path = r"C:\Users\Admin\OneDrive\Dokumente\Projects\Retoflow_Filter-1\TestGround_&_Prototype\TestGround\Test_V7\Test_Test\Test_Dario\Polygon_By_Postal_Code_Extractor_&_Connection_V8_Test\Dash Dash Leaflet\Germany_postal_codes.geojson"

# Load GeoJSON data with geopandas
gdf = gpd.read_file(geojson_file_path)

# Initialize Dash app
app = Dash(__name__)

# Define app layout
app.layout = html.Div([
    dl.Map(dl.TileLayer(), center=[51.3167, 9.5000], zoom=6, style={'height': '50vh'}),
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server()
