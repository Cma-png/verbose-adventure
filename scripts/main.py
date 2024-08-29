import argparse
from backend.core.embedding_service import EmbeddingService

def main():
    parser = argparse.ArgumentParser(description="CLI for Document Search Tool")
    parser.add_argument("--text", type=str, help="Text to embed", required=True)
    
    args = parser.parse_args()
    
    embedding_service = EmbeddingService(model="your_model_here")
    embedding = embedding_service.embed(args.text)
    
    print(f"Generated embedding: {embedding}")

if __name__ == "__main__":
    main()