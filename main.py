from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing import Annotated, Literal
from langchain_core.messages import AnyMessage
from typing import TypedDict

import os
from dotenv import load_dotenv

load_dotenv()


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

class agent_state(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]

load_dotenv()

from supervisor import supervisor_node
from researcher import researcher_node
from developer import developer_node

def route_supervisor(state: agent_state) -> Literal["call_researcher", "call_developer", "finish"]:
    message = state["messages"][-1]
    if isinstance(message, AIMessage) and message.tool_calls:
        return message.tool_calls[0]["name"]
    return "finish"


graph = StateGraph(agent_state)
graph.add_node("supervisor_node", supervisor_node)
graph.add_node("researcher_node", researcher_node)
graph.add_node("developer_node", developer_node)

graph.add_edge(START, "supervisor_node")
graph.add_edge("researcher_node", "supervisor_node")
graph.add_edge("developer_node", "supervisor_node")

graph.add_conditional_edges(
    "supervisor_node",
    route_supervisor,
    {
        "call_researcher": "researcher_node",
        "call_developer": "developer_node",
        "finish": END
    }
)

graph = graph.compile()

if __name__ == "__main__":
    # query = input("Enter your query: ").strip()
    query = "일일 데이터를 이용해서 거래 알고리즘을 구현하고 그 결과를 확인해봐. 데이터 수집은 finance-datareader를 이용해서 하면 돼."
    if not query:
        print("No query provided. Exiting.")
    else:
        result = graph.invoke({"messages": [
            {"role": "user", "content": query}
        ]})
        print("=" * 50)
        print("Final Result")
        print(result["messages"][-1].content)
