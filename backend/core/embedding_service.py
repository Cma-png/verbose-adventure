class EmbeddingService:
    def __init__(self, model):
        self.model = model

    def embed(self, text: str):
        # Logic to generate embedding from the model
        return self.model.encode(text)