from agent.graph import graph
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

output = graph.invoke({"messages": messages})
logger.info(f"Final state: {output}")
for m in output['messages']:
    m.pretty_print()