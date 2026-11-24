from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Literal

from langchain_core.messages import HumanMessage, AIMessage
from app.graphs.chatbot import chat


router = APIRouter(prefix="/api/v1/chat", tags=["Chat"])

class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(min_length=1, max_length=20000)


class ChatRequest(BaseModel):
    question: str = Field(min_length=1, max_length=20000)
    history: list[Message] = Field(default_factory=list)


@router.post("/")
async def chat_endpoint(request: ChatRequest):

    try:
        messages = []

        for item in request.history:
            if item.role == "user":
                messages.append(HumanMessage(content=item.content))
            else:
                messages.append(AIMessage(content=item.content))


        messages.append(
            HumanMessage(content=request.question)
        )

        answer = await chat(messages)

        return {
            "success": True,
            "answer": answer
        }
    except Exception:
        
        raise HTTPException(
            status_code=500,
            detail="Unable to process your question"
        )
