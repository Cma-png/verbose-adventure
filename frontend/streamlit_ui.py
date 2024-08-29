import streamlit as st
import requests
from io import BytesIO
import base64

# Function to upload PDF and convert to vectors
def upload_pdf(file, api_key, index):
    # Example API endpoint for uploading and processing PDF
    upload_url = "http://127.0.0.1:8000/upload"  # Update with your FastAPI endpoint
    headers = {"Authorization": f"Bearer {api_key}"}
    files = {"file_path": (file.name, file, "application/pdf")}
    data = {"index": index}
    
    response = requests.post(upload_url, headers=headers, files=files, data=data)
    return response.json()

# Function to query LLM
def query_llm(query):
    query_url = "http://127.0.0.1:8000/query"  # Update with your FastAPI endpoint
    response = requests.post(query_url, json={"query": query})
    return response.json()

# App title
st.set_page_config(page_title="💬 Document Search Tool")

# Streamlit app layout
st.title("Document Search Tool")

# Sidebar for API key and index
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Pinecone API Key", type="password")
    index = st.text_input("Pinecone Index Name")
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")
    
    if st.button("Upload PDF"):
        if api_key and index and uploaded_file:
            with st.spinner("Uploading and processing PDF..."):
                result = upload_pdf(uploaded_file, api_key, index)
                st.success("PDF uploaded and processed!")
                st.json(result)
        else:
            st.error("Please provide the API key, index, and upload a PDF.")

# Right-hand side for LLM queries
st.header("LLM Chat")
query = st.text_input("Enter your query")

if st.button("Submit Query"):
    if query:
        response = query_llm(query)
        st.json(response)
    else:
        st.error("Please enter a query.")