## From Youtube-CampusX

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import streamlit as st
from langchain.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

chat_model = init_chat_model("openai:gpt-3.5-turbo")

st.header("One-on-One Chatbot using Langchain and Streamlit")

user_input = st.chat_input("write your message here...")


st.set_page_config(page_title="LangChain Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 LangChain Chatbot")
st.caption("A conversational assistant powered by GPT-4o-mini and LangChain")



if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage("""You are a Creative Idea Generator that produces innovative, feasible, and original ideas within a given domain (e.g., AI, robotics, education).
            Use associative thinking, analogy, and pattern recognition to produce ideas that are both novel and practical. You have to be very detailed in your response.
            Respond in an enthusiastic and encouraging tone while still maintaining clarity and structure.
            For each idea, output: Title, Description, Value Proposition, and Potential Challenges."""),
        HumanMessage("Hey! can you help me with an idea?"),
        AIMessage("Of course! You don't have to ask! I am always there for you. Tell me what you need.")
    ]

if user_input:
    # Append user message to session state
    st.session_state.chat_history.append(HumanMessage(user_input))

    # Get model response
    with st.spinner("Thinking..."):
    # Stream response
        chunks = []
        full_message = None

        # Create a streaming container in the UI
        with st.chat_message("assistant"):
            stream_placeholder = st.empty()

            # Stream the model output incrementally
            for chunk in chat_model.stream(st.session_state.chat_history):
                chunks.append(chunk)

                # Merge text chunks as they arrive
                full_message = chunk if full_message is None else full_message + chunk

                # Display partial response (real-time)
                stream_placeholder.markdown(full_message.content)

        # After streaming ends, store the final complete message
    st.session_state.chat_history.append(AIMessage(full_message.content))