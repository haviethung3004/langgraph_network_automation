from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
from langgraph.graph import MessagesState, START, END, StateGraph, add_messages
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv(find_dotenv(), override=True)

# Initialize LLM
llm = ChatOpenAI(model='gpt-4o-mini', api_key=os.getenv('OPENAI_API_KEY'))

# Define node with robust input validation
def chat_model_node(state: MessagesState):
    messages = state.get('messages', [])
    logger.info(f"Input messages: {messages}")
    # Filter out invalid or empty messages
    valid_messages = [
        msg for msg in messages
        if isinstance(msg, (AIMessage, HumanMessage)) and msg.content and msg.content.strip()
    ]
    logger.info(f"Valid messages after filtering: {valid_messages}")
    if not valid_messages:
        logger.warning(f"No valid messages provided; returning default response. Raw input: {state}")
        return {"messages": AIMessage(content="Please provide a non-empty message.")}
    try:
        response = llm.invoke(valid_messages)
        logger.info(f"LLM response: {response}")
        return {"messages": response}
    except Exception as e:
        logger.error(f"LLM error: {str(e)}")
        return {"messages": AIMessage(content=f"Error: {str(e)}")}

# Build graph
builder = StateGraph(MessagesState)
builder.add_node("chat_model", chat_model_node)
builder.add_edge(START, "chat_model")
builder.add_edge("chat_model", END)
graph = builder.compile()
