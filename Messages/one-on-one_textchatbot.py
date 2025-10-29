from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain.messages import SystemMessage, HumanMessage, AIMessage

#Loading API keys from .env file

load_dotenv()

chat_model = init_chat_model(model="openai:gpt-3.5-turbo", temperature=0, max_tokens=500)

while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'quit']:
        print("Chatbot: Goodbye!")
        break

    response = chat_model.invoke(user_input)
    print("Chatbot:", response.content)


