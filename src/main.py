import streamlit as st
from streamlit_chat import message
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
import os
from dotenv import load_dotenv


#Config
st.set_page_config(layout="wide", page_icon="🤖", page_title="AI | Chat-Bot")

#Title
st.markdown(
    """
    <h2 style='text-align: center;'> Your AI Conversation assistant 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")

#Robby's Pages
st.subheader("🚀 AI Conversation KIT's Pages")
st.write("""
- **Chat**: General Chat on data (CSV) with a [vectorstore](https://github.com/facebookresearch/faiss) (index useful parts(max 4) for respond to the user) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html)
""")
st.markdown("---")


if os.path.exists(".env"):
    load_dotenv()
    user_api_key = os.getenv("OPENAI_API_KEY")
    st.sidebar.success("API key loaded from .env", icon="🚀")
    st.session_state.api_key = user_api_key
    
else:
    user_api_key = st.sidebar.text_input(
    label="#### Your OpenAI API key 👇",
    placeholder="Paste your openAI API key, sk-",
    type="password")

with st.sidebar.expander("📬 Contact"):
    st.write("**GitHub:**",
"[vaibhav-chopda/AIConversationKit](https://github.com/vaibhav-chopda/AIConversationKit.git)")
    st.write("**Mail** : vaibhavchopda04@gmail.com")
    st.write("**Created by Vaibhav Chopda**")