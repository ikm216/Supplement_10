from pymongo import MongoClient
import uuid

client = MongoClient("mongodb+srv://ikmclassof22:test@cluster0.vtg6m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsAllowInvalidCertificates=True)
db = client['sample_mflix']
collection = db['users']

def create_a_document():
    document = {
        "UUID": str(uuid.uuid4()),
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 30
    }
    return document["UUID"], document

def test_should_return_created_document():
    uuid_id, document = create_a_document()
    assert isinstance(uuid.UUID(uuid_id, version = 4), uuid.UUID)
    assert document["UUID"] == uuid_id
    assert "name" in document
    assert "email" in document
    assert "age" in document
    assert isinstance(uuid_id, str)
    assert len(uuid_id) == 36
