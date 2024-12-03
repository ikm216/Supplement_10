from pymongo import MongoClient
import uuid

client = MongoClient("mongodb+srv://ikmclassof22:test@cluster0.vtg6m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsAllowInvalidCertificates=True)
db = client['sample_mflix']
collection = db['users']

from test import(
    create_a_document, save_a_document, find_document_uuid, update_document, delete_document
)

def test_should_return_created_document():
    uuid_id = create_a_document()
    assert isinstance(uuid.UUID(uuid_id, version = 4), uuid.UUID)
