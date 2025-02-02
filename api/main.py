from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

import httpx
from bs4 import BeautifulSoup

from services import openai_usage

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8501"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def getContent(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.get_text()
    return content

@app.get("/", response_class = PlainTextResponse)
async def root():
    return "API GPT is Alive"

@app.get("/summary", response_class = PlainTextResponse)
async def summary(url: str):
    content = await getContent(url)
    summary = openai_usage.getSummary(content)
    return summary

@app.get("/answer", response_class = PlainTextResponse)
async def answer(url: str, question: str):
    content = await getContent(url)
    answer = openai_usage.getAnswer(content, question)
    return answer
