from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from pinecone import Pinecone
from dotenv import load_dotenv
import os
from langchain_pinecone import PineconeVectorStore

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')


extracted_data = load_pdf(r"medical_chatbot\data")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

index_name="medical-chatbot"

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index('medical-chatbot')


docsearch = PineconeVectorStore.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)