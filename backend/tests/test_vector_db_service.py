import unittest
from backend.core.vector_db_service import VectorDBService

class TestVectorDBService(unittest.TestCase):
    def test_insert_and_query(self):
        service = VectorDBService(vector_db="mock_db")
        vector = [0.1, 0.2, 0.3]
        service.insert_vector(vector, {"doc_id": 1})
        results = service.query_vector(vector)
        self.assertTrue(len(results) > 0)