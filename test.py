from pymongo import MongoClient
import uuid

client = MongoClient("mongodb+srv://ikmclassof22:test@cluster0.vtg6m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsAllowInvalidCertificates=True)
db = client['sample_mflix']
collection = db['users']

def create_a_document():
    """
    Creates a random MongoDB document and returns its UUID.

    Returns:
        The UUID of the document and the document.
    """
    document = {
        "UUID": str(uuid.uuid4()),
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 30
    }
    return document["UUID"], document

def save_a_document(collection, document):
    answer = collection.insert_one(document)
    return answer.inserted_id

def test_should_return_created_document():
    client = MongoClient("mongodb+srv://ikmclassof22:test@cluster0.vtg6m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsAllowInvalidCertificates=True)
    db = client['sample_mflix']
    collection = db['users']
    uuid_id, document = create_a_document()
    assert isinstance(uuid.UUID(uuid_id, version = 4), uuid.UUID)
    assert document["UUID"] == uuid_id
    assert "name" in document
    assert "email" in document
    assert "age" in document
    assert isinstance(uuid_id, str)
    assert len(uuid_id) == 36

def test_should_save_documet():
    client = MongoClient("mongodb+srv://ikmclassof22:test@cluster0.vtg6m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsAllowInvalidCertificates=True)
    db = client['sample_mflix']
    collection = db['users']
    uuid_id, document = create_a_document()
    saved_document = save_a_document(collection, document)
    assert saved_document is not None


