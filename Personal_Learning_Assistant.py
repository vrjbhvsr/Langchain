from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import streamlit as st
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate, MessagesPlaceholder, load_prompt
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

chat_model = init_chat_model("openai:gpt-5-nano", 
                             temperature = 0.7,
                             max_tokens= 1500,
                             max_retries = 2,
                             timeout= 60)

st.set_page_config(page_title="Personalised Langchain Learning Assistant", page_icon="👨‍🏫", layout= "wide", initial_sidebar_state="expanded")
st.title("Personalised Langchain Learning Assistan👨‍🏫")

human_message = st.chat_input("Ask me something....")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message("user" if isinstance(message, HumanMessage) else "assistant"):
        st.markdown(message.content)

if human_message:
    with st.chat_message("user"):
        st.markdown(human_message)
    st.session_state.chat_history.append(HumanMessage(content=human_message))


for chunk in chat_model.stream()