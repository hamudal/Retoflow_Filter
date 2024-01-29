import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, MultiPolygon
import geojson

def handle_multipolygon(multipolygon):
    if isinstance(multipolygon, MultiPolygon):
        polygons = [Polygon(list(poly.exterior.coords)) for poly in multipolygon.geoms]
        return polygons
    elif isinstance(multipolygon, Polygon):
        return [multipolygon]
    else:
        print(f"Unhandled geometry type: {type(multipolygon)}")
        return []

def postal_code_polygon_dict_extractor(place_name, save_geojson=False):
    postal_code_polygons = ox.features_from_place(place_name, tags={"boundary": "postal_code"})

    gdf = gpd.GeoDataFrame(postal_code_polygons).dropna(subset=['postal_code', 'geometry'])

    postal_code_polygon_dict = {}

    for _, feature in gdf.iterrows():
        postal_code = feature['postal_code']
        geometry = feature['geometry']

        geometries = handle_multipolygon(geometry)

        postal_code_polygon_dict[postal_code] = geometries

    if save_geojson:
        geojson_filename = f"{place_name}_postal_codes.geojson"

        geojson_features = []
        for postal_code, geometries_list in postal_code_polygon_dict.items():
            for geometry in geometries_list:
                coordinates = list(geometry.exterior.coords)

                feature = {
                    "postal_code": postal_code,
                    "geometry": {
                        "type": geometry.geom_type,
                        "coordinates": coordinates
                    }
                }

                geojson_features.append(feature)

        with open(geojson_filename, 'w') as file:
            geojson.dump(geojson_features, file)

        print(f"GeoJSON file saved as: {geojson_filename}")

    return postal_code_polygon_dict

def plot_all_postal_code_polygons(gdf, highlight_postal_code=None, zoom_into_city=False):
    crs = "EPSG:25832"
    
    if zoom_into_city:
        # Get the bounding box of the GeoDataFrame
        bbox = gdf.total_bounds
        margin = 0.1  # 10% margin
        bbox_expanded = [bbox[0] - margin, bbox[1] - margin, bbox[2] + margin, bbox[3] + margin]
        gdf = gdf.cx[bbox_expanded[0]:bbox_expanded[2], bbox_expanded[1]:bbox_expanded[3]]

    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Set the CRS for the GeoDataFrame
    gdf.crs = crs
    
    # Plot the map with the GeoDataFrame and apply the specified projection
    gdf.to_crs(crs).plot(ax=ax, edgecolor='k')

    if highlight_postal_code is not None:
        highlight_geometry = gdf[gdf['postal_code'] == highlight_postal_code].to_crs(crs)
        highlight_geometry.plot(color='red', edgecolor='black', ax=ax)

    # Display the map
    plt.show()
