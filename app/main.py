from fastapi import FastAPI
from pydantic import BaseModel
from app.chatbot import get_answer

app = FastAPI(title="AI CS Top Up Game")


class Question(BaseModel):
    message: str


@app.get("/")
def root():
    return {"status": "ok", "service": "AI CS Top Up Game"}


@app.post("/ask")
def ask(question: Question):
    answer = get_answer(question.message)
    return {"answer": answer}