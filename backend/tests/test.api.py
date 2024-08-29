import unittest
from fastapi.testclient import TestClient
from backend.app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_upload_document(self):
        with open("tests/sample.pdf", "rb") as file:
            response = self.client.post("/upload", files={"file": file})
            self.assertEqual(response.status_code, 200)

    def test_query_documents(self):
        response = self.client.get("/query", params={"query_text": "sample query"})
        self.assertEqual(response.status_code, 200)