# Create server parameters for stdio connection
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv(), override=True)


llm = ChatOpenAI(model='gpt-4o-mini', api_key=os.getenv('OPENAI_API_KEY'))

server_params = StdioServerParameters(
    command="uv",
    args= [
            "run",
            "--with",
            "mcp[cli],netmiko",
            "mcp",
            "run",
            "C:\\Users\\dsu979\\Documents\\MCP_Network_automator\\mcp_cisco_server.py"
        ],)

async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        # Initialize the connection
        await session.initialize()

        # Get tools
        tools = await load_mcp_tools(session)

        # Create and run the agent
        agent = create_react_agent(llm, tools)
        agent_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
