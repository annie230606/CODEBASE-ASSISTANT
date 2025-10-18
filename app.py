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
        ("system","you are a greeter to the user.give polite response to the users input"),
        ("user", "{question}")
    ]
)
st.title("codebase Assistant")
question=st.text_input("What is your Question?")
tab1 = st.tabs(["Ask Question"])

llm=Ollama(model="llama3")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if tab1:
    question = st.text_input("Ask a question:")
    if question:
        st.write(chain.invoke({"question": question}))
