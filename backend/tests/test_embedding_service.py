import unittest
from backend.core.embedding_service import EmbeddingService

class TestEmbeddingService(unittest.TestCase):
    def test_embed(self):
        service = EmbeddingService(model="mock_model")
        embedding = service.embed("test")
        self.assertIsNotNone(embedding)