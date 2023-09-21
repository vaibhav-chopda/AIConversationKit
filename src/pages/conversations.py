import streamlit as st
from langchain.document_loaders.csv_loader import CSVLoader
import tempfile

uploaded_file = st.sidebar.file_uploader("upload", type="csv")

if uploaded_file :
   #use tempfile because CSVLoader only accepts a file_path
   
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    loader = CSVLoader(file_path=tmp_file_path, encoding="utf-8", csv_args={
                'delimiter': ','})
    data = loader.load()