# get_place_postal_code_polygons.py
from common_functions import format_geojson_data, save_geojson_to_file

def get_place_postal_code_polygons(place_name):
    postal_code_polygons = ox.features_from_place(place_name, tags={"boundary": "postal_code"})

    df = pd.DataFrame(postal_code_polygons).dropna(subset=['postal_code', 'geometry'])
    postal_code_polygon_dict = {feature['postal_code']: feature['geometry'] for _, feature in df.iterrows()}
    
    return postal_code_polygon_dict

def main():
    place_input = input("Enter the city or country name: ")

    place_postal_code_polygons = get_place_postal_code_polygons(place_input)
    place_geojson_data = format_geojson_data(place_postal_code_polygons)

    file_name = f"{place_input}_geojson_data.geojson"
    saved_file_path = save_geojson_to_file(place_geojson_data, file_name)

    print(f"{place_input} GeoJSON data saved to {saved_file_path}")

if __name__ == "__main__":
    main()
