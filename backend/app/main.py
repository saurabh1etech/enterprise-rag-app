from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat import router as chat_router

app = FastAPI(
    title="Enterprise RAG Chatbot",
    description="Enterprise AI Knowledge Assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"]
)

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "application": "Enterprise RAG Chatbot"
    }


app.include_router(chat_router)