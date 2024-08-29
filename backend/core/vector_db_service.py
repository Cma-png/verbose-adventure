class VectorDBService:
    def __init__(self, vector_db):
        self.vector_db = vector_db

    def insert_vector(self, vector, metadata):
        # Logic to insert vector into the vector database
        self.vector_db.insert(vector, metadata)

    def query_vector(self, vector, top_k=10):
        # Logic to query the vector database
        return self.vector_db.query(vector, top_k)