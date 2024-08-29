import unittest
from fastapi.testclient import TestClient
from backend.app import app

class TestEndToEnd(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_full_flow(self):
        with open("tests/sample.pdf", "rb") as file:
            upload_response = self.client.post("/upload", files={"file": file})
            self.assertEqual(upload_response.status_code, 200)

        query_response = self.client.get("/query", params={"query_text": "sample query"})
        self.assertEqual(query_response.status_code, 200)