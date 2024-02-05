import json
import geopandas as gpd
from dash import Dash, html, dcc, callback, Output, Input
import dash_leaflet as dl
from dash_extensions.javascript import assign

# Replace the actual file path with your GeoJSON file location
geojson_file_path = r"C:\Users\Admin\OneDrive\Dokumente\Projects\Retoflow_Filter-1\TestGround_&_Prototype\TestGround\Test_V7\Test_Test\Test_Dario\Polygon_By_Postal_Code_Extractor_&_Connection_V8_Test\V8_Dario\Germany_postal_codes.geojson"

# Load GeoJSON data with geopandas
gdf = gpd.read_file(geojson_file_path)

# Extract polygons and multipolygons
polygons = gdf[gdf['geometry'].geom_type == 'Polygon']
multipolygons = gdf[gdf['geometry'].geom_type == 'MultiPolygon']

# Convert GeoDataFrames to GeoJSON format
polygons_geojson = json.loads(polygons.to_json())
multipolygons_geojson = json.loads(multipolygons.to_json())

# Initialize Dash app
app = Dash(__name__)

# Define app layout
app.layout = html.Div([
    dl.Map(
        [
            dl.TileLayer(),
            # Postal code borders with polygons in blue
            dl.GeoJSON(
                data=polygons_geojson,
                id='polygons',
                style={'color': 'blue'},
                hoverStyle=assign("{'fillColor': 'yellow', 'fillOpacity': 0.2}"),
                hideout=dict(type='FeatureCollection', features=[]),  # Initialize hideout
            ),
            # Postal code borders with multipolygons in red
            dl.GeoJSON(
                data=multipolygons_geojson,
                id='multipolygons',
                style={'color': 'red'},
                hoverStyle=assign("{'fillColor': 'orange', 'fillOpacity': 0.2}"),
                hideout=dict(type='FeatureCollection', features=[]),  # Initialize hideout
            ),
        ],
        center=[51.1657, 10.4515],  # Center of Germany
        zoom=6,
        style={'height': '50vh'},
    ),
    # Layer control
    dcc.Checklist(
        options=[
            {'label': 'Polygons', 'value': 'polygons'},
            {'label': 'Multipolygons', 'value': 'multipolygons'},
        ],
        value=['polygons', 'multipolygons'],
        id='layer-control'
    ),
    # Information panel
    html.Div(id='info-panel'),
])

# Define callbacks
@app.callback(
    [
        Output('info-panel', 'children'),
        Output('polygons', 'hideout'),
        Output('multipolygons', 'hideout'),
        Output('polygons', 'hideout'),
        Output('multipolygons', 'hideout'),
    ],
    [
        Input('polygons', 'featureHover'),
        Input('multipolygons', 'featureHover'),
        Input('layer-control', 'value')
    ]
)
def update_info_panel(polygons_hover, multipolygons_hover, selected_layers):
    # Initialize hideouts
    polygons_hideout = dict(type='FeatureCollection', features=[])
    multipolygons_hideout = dict(type='FeatureCollection', features=[])

    if 'polygons' in selected_layers:  # Show polygons
        polygons_hideout['features'] = polygons_geojson['features']  # Enable polygons
    else:  # Hide polygons
        pass  # Hideout already initialized with empty features

    if 'multipolygons' in selected_layers:  # Show multipolygons
        multipolygons_hideout['features'] = multipolygons_geojson['features']  # Enable multipolygons
    else:  # Hide multipolygons
        pass  # Hideout already initialized with empty features

    # Update information panel based on hover events
    if polygons_hover:
        feature = polygons_hover[0]
        postal_code = feature['properties'].get('postal_code', 'N/A')
        return f"Postal Code: {postal_code}", polygons_hideout, multipolygons_hideout, {}, {}
    elif multipolygons_hover:
        feature = multipolygons_hover[0]
        postal_code = feature['properties'].get('postal_code', 'N/A')
        return f"Postal Code: {postal_code}", polygons_hideout, multipolygons_hideout, {}, {}
    else:
        return "Hover over a feature to see details.", polygons_hideout, multipolygons_hideout, {}, {}



if __name__ == '__main__':
    app.run_server(debug=True)
