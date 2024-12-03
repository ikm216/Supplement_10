from pymongo import MongoClient
import uuid

def test_connection():

    try:
        client = MongoClient("mongodb+srv://ikmclassof22:test@cluster0.vtg6m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsAllowInvalidCertificates=True)
        db = client['sample_mflix']
        collection = db.list_collection_names()

        print("Connection successful!")
        print("Collections in the database:", collection)
        
        return True
    except Exception as e:
        print("Connection failed:", e)
        return False

# Test the connection
if __name__ == "__main__":
    test_connection()