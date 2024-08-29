import unittest
import time
from fastapi.testclient import TestClient
from backend.app import app

class TestLoad(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_load_handling(self):
        start_time = time.time()

        for _ in range(100):
            response = self.client.get("/query", params={"query_text": "load test"})
            self.assertEqual(response.status_code, 200)

        end_time = time.time()
        duration = end_time - start_time
        print(f"Processed 100 requests in {duration} seconds")