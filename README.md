# LangGraph Network Automation

A framework for automating network operations and management using LangGraph and large language models.

## Overview

This project leverages LangGraph to create conversational AI agents capable of automating network management tasks. Built with LangChain and OpenAI's models, it provides a structured framework for developing network automation workflows.

## Features

- Conversational interface for network management
- Modular graph-based architecture using LangGraph
- Support for multiple LLM backends (OpenAI, Google Gemini)
- Extensible design for adding custom automation workflows

## Requirements

- Python 3.13+
- OpenAI API key (for GPT models)
- Network devices accessible via standard protocols

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd langgraph_network_automation
```

2. Install dependencies:
```bash
pip install -e .
```

3. Create an `.env` file with your API keys:
```
OPENAI_API_KEY=your_api_key_here
```

## Quick Start

1. Make sure your environment variables are set up correctly in `.env`
2. Run the main application:
```bash
python main.py
```

## Project Structure

```
langgraph_network_automation/
├── src/
│   └── agent/
│       └── agent.py      # Main agent implementation
├── main.py               # Entry point for the application
├── langgraph.json        # LangGraph configuration
├── pyproject.toml        # Project dependencies
└── README.md             # This file
```

## Development

### Adding New Capabilities

To add new automation capabilities:

1. Create a new node in the LangGraph state machine
2. Implement the corresponding function that performs the network task
3. Update the graph structure to include your new node

Example:
```python
def network_config_node(state: MessagesState):
    # Your network configuration logic here
    return {"messages": [AIMessage(content="Network configured successfully")]}

# Add to graph
builder.add_node("network_config", network_config_node)
builder.add_edge("chat_model", "network_config")
```

## License

[Add your license information here]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
