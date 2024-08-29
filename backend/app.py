from fastapi import FastAPI
from backend.api import document_router, query_model

app = FastAPI()

app.include_router(document_router.router)
app.include_router(query_model.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Search Tool API"}