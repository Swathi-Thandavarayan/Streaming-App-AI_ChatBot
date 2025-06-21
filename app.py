# app.py

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("🤖 Gemini Chatbot with LangChain")

#3 getting response
def get_response(query, chat_history):
    template = """
    You are a helpful, friendly AI assistant in a chat. Respond conversationally and naturally.

    Here is the previous conversation:

    Chat history: {chat_history}

    User question: {user_question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    chain = prompt | llm | StrOutputParser()

    return chain.stream({
        "chat_history": chat_history,
        "user_question": query
    })


#for conversation
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)

    else:
        with st.chat_message("AI"):
            st.markdown(message.content)       
#1 user input
user_query = st.chat_input("Your message")
if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        ai_response = st.write_stream(get_response(user_query,st.session_state.chat_history)) 
         


    st.session_state.chat_history.append(AIMessage(ai_response))    
