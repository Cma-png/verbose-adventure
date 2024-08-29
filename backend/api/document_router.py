from fastapi import APIRouter, UploadFile, File
from backend.core.pdf_loader import PDFLoader
from backend.core.text_cleaner import TextCleaner
from backend.core.embedding_service import EmbeddingService
from backend.core.vector_db_service import VectorDBService

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    pdf_loader = PDFLoader(file.file)
    text = pdf_loader.extract_text()
    
    text_cleaner = TextCleaner()
    cleaned_text = text_cleaner.clean(text)
    
    embedding_service = EmbeddingService(model="your_model_here")
    embedding = embedding_service.embed(cleaned_text)
    
    vector_db_service = VectorDBService(vector_db="your_db_here")
    vector_db_service.insert_vector(embedding, {"filename": file.filename})
    
    return {"message": "Document uploaded and vector stored successfully."}