from pymongo import MongoClient
from pymongo import ReturnDocument
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
        "email": f"john.doe.{uuid.uuid4().hex[:8]}@example.com",
        "age": 30
    }
    return document["UUID"], document

def save_a_document(collection, document):
    """
    Saves a document to the MongoDB collection.

    Args:
        collection: MongoDB collection to insert the document.
        document: The document to save.

    Returns:
        The ID of the inserted document.
    """
    answer = collection.insert_one(document)
    return answer.inserted_id

def find_a_document_uuid(collection, uuid_id):
     """
    Finds a document in the MongoDB collection by its UUID.

    Args:
        collection: MongoDB collection to search.
        uuid_id: The UUID of the document to find.

    Returns:
        The found document or None if not found.
    """
     return collection.find_one({"UUID": uuid_id})

def update_a_document(collection, uuid_id, field, val):
    """
    Updates a specific field in a MongoDB document identified by UUID.

    Args:
        collection: MongoDB collection.
        uuid_id: UUID of the document to update.
        field: Field to update in the document.
        val: New value for the field.

    Returns:
        The updated document.
    """
    doc = collection.find_one_and_update({"UUID": uuid_id}, {"$set": {field: val}}, return_document = ReturnDocument.AFTER)
    return doc

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

def test_should_find_a_document():
    client = MongoClient("mongodb+srv://ikmclassof22:test@cluster0.vtg6m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsAllowInvalidCertificates=True)
    db = client['sample_mflix']
    collection = db['users']

    uuid_id, document = create_a_document()
    saved_document = save_a_document(collection, document)

    find_document = find_a_document_uuid(collection, uuid_id)
    
    assert find_document is not None
    assert find_document["UUID"] == uuid_id

def test_should_update_a_document():
    client = MongoClient("mongodb+srv://ikmclassof22:test@cluster0.vtg6m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsAllowInvalidCertificates=True)
    db = client['sample_mflix']
    collection = db['users']

    uuid_id, document = create_a_document()
    saved_document = save_a_document(collection, document)

    updated_document = update_a_document(collection, uuid_id, "age", 25)
    assert updated_document["age"] == 25

def test_should_delete_a_document():
    client = MongoClient("mongodb+srv://ikmclassof22:test@cluster0.vtg6m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsAllowInvalidCertificates=True)
    db = client['sample_mflix']
    collection = db['users']

    uuid_id, document = create_a_document()
    saved_document = save_a_document(collection, document)

    delete = delete_a_document(collection, uuid_id)
    assert delete == 1

    verify = find_a_document_uuid(collection, uuid_id)
    assert verify is None




