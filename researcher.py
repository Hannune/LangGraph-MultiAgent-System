import asyncio
from gpt_researcher import GPTResearcher
from langchain_core.messages import AIMessage
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["FAST_LLM"]="openai:gpt-4o-mini"
os.environ["SMART_LLM"]="openai:gpt-4o-mini"
os.environ["STRATEGIC_LLM"]="openai:gpt-4o-mini"
os.environ["EMBEDDING"]="openai:text-embedding-3-small"
os.environ["TAVILY_API_KEY"]=os.getenv("TAVILY_API_KEY")



def run_researcher_sync(query: str, report_type: str = "research_report") -> str:
    """
    Synchronous wrapper for GPT Researcher.
    """
    async def async_research():
        researcher = GPTResearcher(query=query, report_type=report_type)
        await researcher.conduct_research()
        return await researcher.write_report()
    
    return asyncio.run(async_research())


def researcher_node(state):
    print("researcher_node===========================")
    messages = state["messages"]
    last_message = messages[-1]
    print(f"last_message: {last_message}")
    query = last_message.content  # Only use the last message (from supervisor or initial query)
    result = run_researcher_sync(query)

    print(f"result: {result}")
    print("researcher_node---------------------------")


    return {"messages": [AIMessage(content=f"Research Report:\n{result}")]}
