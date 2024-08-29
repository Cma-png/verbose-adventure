# Document Search and Analysis Tool

A powerful tool for document search and analysis using advanced language models. Upload PDFs, convert them to vectors, and query your documents with ease.

https://github.com/user-attachments/assets/1161b9f2-7f42-4cc5-b15e-da7f1f6401c3

## Features

- **PDF Upload and Vectorization**: Upload PDFs and convert them into vectors using Pinecone.
- **Advanced Querying**: Leverage the Ollama model for intelligent document querying.
- **User-Friendly Interface**: Built with Streamlit for a seamless user experience.

<div style="display: flex; justify-content: center;">
  <img width="350" alt="Untitled" src="https://github.com/user-attachments/assets/3ca2d5a2-dfec-47b6-96c4-47d25fe66359">
  <img width="350" alt="Untitled2" src="https://github.com/user-attachments/assets/008503f9-00f4-4442-90b3-f49ce2357b56">
</div>

## Quick Start

### Prerequisites

- Python 3.10
- Docker
- Pinecone API Key
- Ollama Model (pre-configured in the application)

### Setup

#### 1. Create a Pinecone Account and API Key

1. Sign up for a Pinecone account at [Pinecone](https://www.pinecone.io/).
2. Create an index and generate your API key.
3. Save your API key and index name, as you'll need them to run the application.

#### 2. Configure the Models in the Code

1. Open `backend/core/embedding_service.py`.
2. Find the section where the models are defined:

```python
   # Example configuration
   LLM_MODEL_NAME = "your_llm_model_name"
   EMBEDDING_MODEL_NAME = "your_embedding_model_name"
```
3. Replace "your_llm_model_name" and "your_embedding_model_name" with the actual names of the models you downloaded.



### 4. Build and Run
#### 4.1. With Docker

1. Ensure Docker is installed on your system. 
2.	From the project root, run:
```bash
docker-compose up --build
```
3.	Access the app at `http://localhost:8501`.


#### 4.2. Without Docker
1. Install dependencies:
```bash
pip install -r backend/requirements.txt
```
2. Start the FastAPI server:
```bash
python backend/scripts/main.py
```
3. In a new terminal, start the Streamlit frontend:
```
streamlit run frontend/streamlit_ui.py
```
4. 	Open `http://localhost:8501` to use the app.

### 5. Enter Pinecone API Key and Index to Use
After starting the Streamlit frontend, enter the Pinecone API key and index:
<img width="388" alt="Untitled" src="https://github.com/user-attachments/assets/4c65e441-d134-4713-9677-e3885b5323c1">

### 6. Upload your document pdf
+ Push the buttom to convert your pdf to vector and store to the vectorDB
+ Now, you may start to ask the llm question about your pdf
<img width="1045" alt="Untitled 2" src="https://github.com/user-attachments/assets/a41c9e3a-c9e3-4082-ad8a-e37652142a4e">


