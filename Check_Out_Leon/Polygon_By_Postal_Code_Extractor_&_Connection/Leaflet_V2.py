import json
import geopandas as gpd
from dash import Dash, html, dcc, callback, Output, Input, State
import dash_leaflet as dl

# (Ger) Replace the actual file path with your GeoJSON file location
geojson_file_path = r"C:\Users\Admin\OneDrive\Dokumente\Projects\Retoflow_Filter-1\TestGround_&_Prototype\TestGround\Test_V7\Test_Test\Test_Dario\Polygon_By_Postal_Code_Extractor_&_Connection_V8_Test\V8_Dario\Germany_postal_codes.geojson"

#geojson_file_path = r"C:\Users\Admin\OneDrive\Dokumente\Projects\Retoflow_Filter-1\Check_Out_Leon\Polygon_By_Postal_Code_Extractor_&_Connection\Kassel_postal_codes.geojson"

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
                hoverStyle={'fillColor': 'yellow', 'fillOpacity': 0.1},
                hideout=dict(type='FeatureCollection', features=[]),
            ),
            # Postal code borders with multipolygons in red
            dl.GeoJSON(
                data=multipolygons_geojson,
                id='multipolygons',
                style={'color': 'red'},
                hoverStyle={'fillColor': 'orange', 'fillOpacity': 0.1},
                hideout=dict(type='FeatureCollection', features=[]),
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
    ],
    [
        Input('polygons', 'featureClick'),
        Input('multipolygons', 'featureClick'),
        Input('layer-control', 'value'),
    ],
    [
        State('polygons', 'hideout'),
        State('multipolygons', 'hideout'),
    ]
)
def update_info_panel(polygons_click, multipolygons_click, layers, polygons_hideout, multipolygons_hideout):
    selected_layer = []
    if 'polygons' in layers:
        selected_layer.append(polygons_geojson)
    if 'multipolygons' in layers:
        selected_layer.append(multipolygons_geojson)

    selected_hideout = polygons_hideout if 'polygons' in layers else multipolygons_hideout

    if polygons_click:
        feature = polygons_click['properties']
        postal_code = feature.get('postal_code', 'N/A')
        selected_hideout['features'] = [poly for poly in polygons_geojson['features'] if poly['properties'] == feature]  # Update hideout
        return f"Postal Code: {postal_code}", selected_hideout, selected_layer
    elif multipolygons_click:
        feature = multipolygons_click['properties']
        postal_code = feature.get('postal_code', 'N/A')
        selected_hideout['features'] = [multi for multi in multipolygons_geojson['features'] if multi['properties'] == feature]  # Update hideout
        return f"Postal Code: {postal_code}", selected_hideout, selected_layer
    else:
        return "Click on a feature to see details.", selected_hideout, selected_layer

if __name__ == '__main__':
    app.run_server(debug=True)
