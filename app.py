import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
load_dotenv()
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY" )
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT" )

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are an expert at codebase assisting. Please explain any doubts user has about the input"),
        ("user", "{question}")
    ]
)
st.title("codebase Assistant")
question=st.text_input("What is your Question?")
tab1, tab2, tab3 = st.tabs(["❓ Ask Question", "📋 Paste Code", "📂 Upload File"])

llm=Ollama(model="gemma3:1b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if tab1:
    question = st.text_input("Ask a programming question:")
    if question:
        st.write(chain.invoke({"question": question}))
if tab2:
    code=st.text_area("paste your code here")
    if code:
        query = f"Explain this code and suggest improvements:\n{code}"
        st.write(chain.invoke({"question": query}))
if tab3:
    file=st.file_uploader("Upload the required file")
    if file:
        query=f"Analyze this code file and explain what it does. Suggest improvements if possible:\n{file}"
        st.write(chain.invoke({"question": query}))
