from fastapi import APIRouter, Query
from backend.core.embedding_service import EmbeddingService
from backend.core.vector_db_service import VectorDBService

router = APIRouter()

@router.get("/query")
async def query_documents(query_text: str = Query(...)):
    embedding_service = EmbeddingService(model="your_model_here")
    embedding = embedding_service.embed(query_text)
    
    vector_db_service = VectorDBService(vector_db="your_db_here")
    results = vector_db_service.query_vector(embedding)
    
    return {"results": results}