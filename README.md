# LangGraph-Supervisor-Agent-System

A LangGraph-based multi-agent system that coordinates between a researcher agent and a developer agent to handle complex tasks requiring both information gathering and code execution.

## Overview

This project implements a supervisor pattern using LangGraph to orchestrate specialized AI agents. The supervisor intelligently routes tasks to either a researcher (for information gathering) or a developer (for code implementation and execution) based on the user's query.

### Architecture

The system consists of three main agents:

- **Supervisor Agent**: Analyzes tasks and delegates to appropriate specialist agents
- **Researcher Agent**: Conducts web research using GPT Researcher and Tavily API
- **Developer Agent**: Executes code and implements solutions using Open Interpreter

## Features

- **Intelligent Task Routing**: Supervisor automatically determines whether research or development is needed
- **Web Research**: Deep research capabilities powered by GPT Researcher and Tavily search
- **Code Execution**: Safe code execution and implementation via Open Interpreter
- **State Management**: Persistent conversation state using LangGraph's message passing
- **Multi-turn Conversations**: Agents can collaborate across multiple turns until task completion

## Installation

### Prerequisites

- Python 3.8+
- OpenAI API key
- Tavily API key

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp file.env.template .env
```

4. Edit `.env` and add your API keys:
```
OPENAI_API_KEY=your_openai_key_here
TAVILY_API_KEY=your_tavily_key_here
```

## Dependencies

The project requires the following packages:

- `langchain` - LangChain framework
- `langgraph` - Graph-based agent orchestration
- `langchain-openai` - OpenAI integration
- `gpt-researcher` - Research agent capabilities
- `open-interpreter` - Code execution
- `finance-datareader` - Financial data access

## Usage

### Basic Example

Run the main script with a predefined query:

```bash
python main.py
```

### Custom Queries

Modify the query in `main.py`:

```python
query = "Your task here"
result = graph.invoke({"messages": [
    {"role": "user", "content": query}
]})
```

### Example Task

The default example demonstrates financial algorithm development:

```python
query = "일일 데이터를 이용해서 거래 알고리즘을 구현하고 그 결과를 확인해봐. 데이터 수집은 finance-datareader를 이용해서 하면 돼."
```

This task requires both research (understanding algorithms) and development (implementing and testing code).

## Project Structure

```
.
├── main.py                 # Entry point and graph orchestration
├── supervisor.py           # Supervisor agent with routing logic
├── researcher.py           # Research agent using GPT Researcher
├── developer.py            # Development agent using Open Interpreter
├── requirements.txt        # Python dependencies
└── file.env.template      # Environment variable template
```

## How It Works

### Workflow

1. User submits a query to the supervisor
2. Supervisor analyzes the task and calls appropriate tool (`call_researcher`, `call_developer`, or `finish`)
3. Specialist agent processes the task and returns results
4. Results flow back to supervisor for next action
5. Process repeats until supervisor calls `finish`

### Agent Details

**Supervisor**:
- Uses GPT-4o-mini with tool calling
- Routes based on conversation history and task requirements
- Provides clear instructions to downstream agents

**Researcher**:
- Leverages GPT Researcher for comprehensive web research
- Uses multiple LLM configurations (FAST_LLM, SMART_LLM, STRATEGIC_LLM)
- Returns structured research reports

**Developer**:
- Executes code via Open Interpreter
- Handles implementation and testing tasks
- Returns development outputs and results

## Configuration

### LLM Models

Both agents use `gpt-4o-mini` by default. You can modify the models in:

- `supervisor.py`: Line with `ChatOpenAI(model="gpt-4o-mini")`
- `researcher.py`: Environment variables for LLM selection
- `developer.py`: `interpreter.llm.model = "openai:gpt-4o-mini"`

### Temperature Settings

Supervisor temperature is set to 0.2 for more consistent routing decisions.

## Troubleshooting

- Ensure all API keys are correctly set in `.env` file
- Check that all dependencies are installed from `requirements.txt`
- For Open Interpreter issues, verify the model name format is correct

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]

---

Built with LangGraph, LangChain, GPT Researcher, and Open Interpreter.
