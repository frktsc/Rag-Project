from medical_chatbot.src.helper import download_hugging_face_embeddings
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from dotenv import load_dotenv
from medical_chatbot.src.prompt import *
import os
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain.chains.question_answering import load_qa_chain
from langchain.schema import Document


load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

embeddings = download_hugging_face_embeddings()


pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index('medical-chatbot') 

index_name="medical-chatbot"


vectorstore = PineconeVectorStore(index=index, embedding=embeddings)  

PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])


llm=CTransformers(model="medical_chatbot\model\llama-2-7b-chat.ggmlv3.q4_0 (1).bin",
                    model_type="llama",
                    config={'max_new_tokens':512,
                            'temperature':0.8})


def retrieve_query(query, k=2):
    matching_results = vectorstore.similarity_search(query, k=k)
    if matching_results:
        best_match_content = matching_results[0].page_content
        best_document = Document(page_content=best_match_content)
        return [best_document] 
    else:
        return []


def retrieve_answers(query):
    try:
        qa=load_qa_chain(llm=llm,chain_type="stuff",prompt=PROMPT)
        query_text = query["query"]
        doc_search = retrieve_query(query_text)
        response = qa.invoke({"input_documents": doc_search, "question": query_text})
        return response
    except Exception as e:
        print(f"Error: {e}")
        return {"result": "Bir hata oluştu."}
