from langchain_openai import ChatOpenAI
from interpreter import interpreter  # Assuming OpenInterpreter is imported as 'interpreter'
from langchain_core.messages import AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

interpreter.llm.model = "openai:gpt-4o-mini"
interpreter.llm.api_key = os.getenv("OPENAI_API_KEY")

def developer_node(state):
    print("developer_node===========================")
    messages = state["messages"].content
    last_message = messages[-1]
    print(f"last_message: {last_message}")
    task = last_message.content  # Only use the last message (from supervisor or initial query)
    
    # Use OpenInterpreter to handle the development task
    output = interpreter.chat(task)  # Assuming chat for conversational development tasks
    print(f"output: {output}")
    print("developer_node---------------------------")

    return {"messages": [AIMessage(content=f"Development Output:\n{output}")]}

# Note: If you need code execution specifically, replace interpreter.chat(task) with interpreter.run(task)
