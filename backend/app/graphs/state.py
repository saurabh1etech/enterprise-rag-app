from langgraph.graph import MessagesState

class ChatbotState(MessagesState):
    """
    State shared between LangGraph nodes.

    MessagesState provides a messages list and
    automatically manages message updates.
    """
    pass