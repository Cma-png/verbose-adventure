# verbose-adventure
Document Search and Analysis Tool


document_search_tool/
├── backend/
│   ├── src/
│   │   ├── main.py
│   │   ├── utils/
│   │   │   ├── pdf_loader.py
│   │   │   ├── text_cleaner.py
│   │   ├── services/
│   │   │   ├── embedding_service.py
│   │   │   ├── vector_db_service.py
│   │   ├── models/
│   │   │   ├── document_model.py
│   │   ├── routers/
│   │   │   ├── document.py
│   │   │   ├── pinecone.py
│   ├── config.py
│   └── requirements.txt
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
└── README.md
