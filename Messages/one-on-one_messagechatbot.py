from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

chat_model = init_chat_model(model="openai:gpt-3.5-turbo", temperature=0.5, max_tokens=500)

system_message = SystemMessage('''You are a Creative Idea Generator that produces innovative, feasible, and original ideas within a given domain (e.g., AI, robotics, education).
Use associative thinking, analogy, and pattern recognition to produce ideas that are both novel and practical. You have to be very detailed in your response.
Respond in an enthusiastic and encouraging tone while still maintaining clarity and structure.
For each idea, output: Title, Description, Value Proposition, and Potential Challenges.''')

human_message = HumanMessage("Hey! can you help me with an idea?")
aiMessage = AIMessage("Ofcourse! You don't have to ask! I am always there for you.Tell me what you need.")




while True:
    messages = [system_message, human_message, aiMessage, HumanMessage(input("You: "))]
    if messages[-1].content.lower() in ['bye', 'quit']:
        print("Chatbot: Goodbye!")
        break
    chunks = []
    full_message = None
    for chunk in chat_model.stream(messages):
        chunks.append(chunk)
        print(chunk.text, end='', flush=True)
        full_message = chunk if full_message is None else full_message + chunk

