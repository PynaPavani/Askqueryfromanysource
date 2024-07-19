import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from langchain_community.chat_models import ChatOllama
from langchain.agents import create_openai_tools_agent
from langchain.agents import AgentExecutor
from langchain import hub
import json

st.title('Web-based Query Response Application')

# User input for three website URLs
url1 = st.text_input('Enter the first website URL:')
url2 = st.text_input('Enter the second website URL:')
url3 = st.text_input('Enter the third website URL:')

if st.button('Create Retrievers'):
    # Load and split documents from each URL
    def load_and_split(url):
        loader = WebBaseLoader(url)
        docs = loader.load()
        return RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(docs)

    documents1 = load_and_split(url1)
    documents2 = load_and_split(url2)
    documents3 = load_and_split(url3)

    # Create vector stores
    vectordb1 = FAISS.from_documents(documents1, OllamaEmbeddings())
    vectordb2 = FAISS.from_documents(documents2, OllamaEmbeddings())
    vectordb3 = FAISS.from_documents(documents3, OllamaEmbeddings())

    # Create retriever tools
    retriever1 = vectordb1.as_retriever()
    retriever_tool1 = create_retriever_tool(retriever1, "Search_1", f"Search for information on {url1}.")
    
    retriever2 = vectordb2.as_retriever()
    retriever_tool2 = create_retriever_tool(retriever2, "Search_2", f"Search for information on {url2}.")
    
    retriever3 = vectordb3.as_retriever()
    retriever_tool3 = create_retriever_tool(retriever3, "Search_3", f"Search for information on {url3}.")

    # Combine tools
    tools = [retriever_tool1, retriever_tool2, retriever_tool3]

    # Store the tools in session state for later use
    st.session_state.tools = tools
    st.success("Retrievers created successfully!")

if 'tools' in st.session_state:
    # Load LLM and prompt
    llm = ChatOllama(model="llama2", temperature=0.7)
    prompt = hub.pull("hwchase17/openai-functions-agent")

    # Create agent
    agent = create_openai_tools_agent(llm, st.session_state.tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=st.session_state.tools, verbose=True)

    # User input for the query
    user_query = st.text_input('Enter your query:')

    if user_query and st.button('Get Response'):
        result = agent_executor.invoke({"input": user_query})
        response = json.dumps(result)
        st.write(response)
