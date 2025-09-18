
import os
from dotenv import load_dotenv
load_dotenv()
# os.environ["OPENAI_API_KEY"]=os.getenv("Open_API_Key")
## Lang smith tracking
os.environ["Langchain_api_key"]=os.getenv("Langchain_api_key")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["Langchain_project"]=os.getenv("Langchain_project")
os.environ["HF_token"]=os.getenv("HF_token")
import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

## Promt Template 
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are helpful assistant .please respond to the questions asked"),
        ("user","Question:{question}")
    ]
)
## Stremlot Framework
st.title("Langchain Demo With Gemma:2b")
input_text=st.text_input("what question you have in  mind?")

## Ollama Llama2 model
llm = OllamaLLM(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
    