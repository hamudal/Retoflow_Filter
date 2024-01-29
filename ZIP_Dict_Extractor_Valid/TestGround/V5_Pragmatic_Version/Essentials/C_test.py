from pymongo import MongoClient
import json

class MongoDBConnector:
    def __init__(self, database_name, collection_name):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def connect_to_local_mongodb(self):
        print("Connected to local MongoDB")
        return self.client, self.collection

    def insert_geojson_data(self, geojson_file_path, chunk_size=1000):
        with open(geojson_file_path, 'r') as file:
            geojson_data = json.load(file)

        # Assuming GeoJSON is a list of features directly
        features = geojson_data
        for i in range(0, len(features), chunk_size):
            chunk = features[i:i+chunk_size]
            self.collection.insert_many(chunk)
            print(f"Inserted {len(chunk)} features into local MongoDB collection '{self.collection.name}'.")

    def close_connection(self):
        self.client.close()
        print("Closed MongoDB connection.")

# Example usage of the class
def insert_geojson_to_mongodb(database_name, collection_name, geojson_file_path, chunk_size=1000):
    # Create an instance of MongoDBConnector
    mongo_connector = MongoDBConnector(database_name, collection_name)

    # Connect to MongoDB
    mongo_client, mongo_collection = mongo_connector.connect_to_local_mongodb()

    # Insert GeoJSON data into MongoDB
    mongo_connector.insert_geojson_data(geojson_file_path, chunk_size)

    # Close MongoDB connection when done
    mongo_connector.close_connection()

if __name__ == "__main__":
    # User input for the database and collection names
    database_name = "ZIP_Poly_Ger_Test"
    collection_name = "ZIP_Poly_Ger_Collection_Test"

    # Example GeoJSON file path
    geojson_file_path = 'Germany_postal_codes.geojson'  # Update the file path accordingly

    # Call the function to insert GeoJSON data into MongoDB
    insert_geojson_to_mongodb(database_name, collection_name, geojson_file_path, chunk_size=1000)
