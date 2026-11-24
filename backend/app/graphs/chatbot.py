from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage

from langgraph.graph import StateGraph, START, END

from app.graphs.state import ChatbotState
from app.core.config import settings


llm = ChatOpenAI(
    model=settings.OPENAI_MODEL,
    temperature=0.2,
    api_key=settings.OPENAI_API_KEY
)


# 2. Define the system instructions
SYSTEM_PROMPT = """
You are an enterprise AI assistant.

Your responsibilities:
- Provide clear and accurate answers.
- Explain technical concepts with examples.
- Avoid making unsupported claims.
- If you don't know something, say so.
"""


async def generate_response(state: ChatbotState):
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        *state["messages"]
    ]

    response = await llm.ainvoke(messages)

    return {
        "messages": [response]
    }

# Build the graph

builder = StateGraph(ChatbotState)

builder.add_node(
    "generate_response", generate_response
)

builder.add_edge(START, "generate_response")
builder.add_edge("generate_response", END)

chatbot_graph = builder.compile()

async def chat(messages):
    result = await chatbot_graph.ainvoke({
         "messages": messages
    })

    return result["messages"][-1].content


