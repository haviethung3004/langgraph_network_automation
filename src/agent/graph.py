#graph.py
from contextlib import asynccontextmanager
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv(find_dotenv(), override=True)

# Initialize LLM
llm = ChatOpenAI(model='gpt-4o-mini', api_key=os.getenv('OPENAI_API_KEY'))

@asynccontextmanager
async def make_graph():
    try:
        logger.info("Starting MCP client setup...")
        mcp_config = {
            "Cisco-IOS-config": {
                "command": "python",
                "args": [
                    "-m",
                    "mcp",
                    "run",
                    "--with",
                    "mcp[cli],netmiko",
                    "C:\\Users\\dsu979\\Documents\\MCP_Network_automator\\mcp_cisco_server.py"
                ],
                "transport": "stdio",
            },
            "perplexity-mcp": {
                "command": "uvx",
                "args": ["C:\\Users\\dsu979\\Documents\\perplexity-mcp"],
                "env": {
                    "PERPLEXITY_API_KEY": "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",
                    "PERPLEXITY_MODEL": "sonar"
                },
                "transport": "stdio",
            },
        }
        logger.info(f"MCP configuration: {mcp_config}")
        
        async with MultiServerMCPClient(mcp_config) as client:
            logger.info("MCP client setup successful!")
            agent = create_react_agent(llm, client.get_tools())
            logger.info("Agent created successfully!")
            yield agent
    except Exception as e:
        logger.error(f"Error in make_graph: {str(e)}")
        raise

