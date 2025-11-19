from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage
from typing import Literal

SYSTEM_PROMPT = """
You are a supervisor agent coordinating a researcher (for gathering information and reports) and a developer (for coding, implementation, or execution tasks). 
Analyze the conversation history and the latest task. Decide if more research is needed, if development/execution is required, or if the task is complete. 
Use the 'call_researcher' tool to delegate research tasks, 'call_developer' for development tasks, or 'finish' to end and summarize the final output.
Provide clear instructions in your response content for the chosen agent.
"""

@tool
def call_researcher(query: str) -> str:
    """Call the researcher agent to conduct research on the given query."""
    return f"Delegating research task: {query}"

@tool
def call_developer(task: str) -> str:
    """Call the developer agent to implement or execute the given task."""
    return f"Delegating development task: {task}"

@tool
def finish(summary: str) -> str:
    """Finish the workflow and provide a final summary."""
    return f"Task complete. Summary: {summary}"

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
tools = [call_researcher, call_developer, finish]
llm_with_tools = llm.bind_tools(tools)

def supervisor_node(state):
    print("supervisor_node===========================")
    messages = state["messages"]
    system_message = {"role": "system", "content": SYSTEM_PROMPT}
    messages = [system_message] + messages

    print(f"messages: {messages}")

    response = llm_with_tools.invoke(messages)
    print(f"response: {response}")
    print("supervisor_node---------------------------")

    return {"messages": [response]}
