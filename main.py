import asyncio
from agent.graph import make_graph
from langchain_core.messages import AIMessage, HumanMessage
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

messages = [
    AIMessage(content="Hi, how are you?"),
    HumanMessage(content="I am doing well, thank you!"),
    AIMessage(content="That's great to hear! How can I assist you today?"),
    HumanMessage(content="I need help with my project.")
]

async def main():
    async with make_graph() as agent:
        output = await agent.ainvoke({"messages": messages})
        logger.info(f"Final state: {output}")
        for m in output['messages']:
            m.pretty_print()

if __name__ == "__main__":
    asyncio.run(main())