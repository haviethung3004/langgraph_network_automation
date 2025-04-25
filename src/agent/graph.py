from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_handoff_tool, create_supervisor

model = ChatOpenAI(model="gpt-4o-mini")

def add(x, y):
    """
    Adds two numbers.
    """
    return x + y

def multiply(x, y):
    """
    Multiplies two numbers.
    """
    return x * y

def web_research(query):
    """
    Searches the web for information.
    """
    return "The weather is sunny today in Ho Chi Minh city."


math_agent = create_react_agent(
    model=model,
    tools=[add, multiply],
    name="math_expert"
)

research_agent = create_react_agent(
    model=model,
    tools=[web_research],
    name="research_expert"
)

supervisor_workflow = create_supervisor(
    [math_agent, research_agent],
    model=model,
    tools=[
        create_handoff_tool(
            agent_name="math_expert",
            description="A math expert that can add and multiply numbers.",
            name="assign_to_math_expert",
        ),
        create_handoff_tool(
            agent_name="research_expert",
            description="A research expert that can search the web for information.",
            name="assign_to_research_expert",
        ),
    ]
)

agent = supervisor_workflow.compile()
