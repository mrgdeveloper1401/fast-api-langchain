from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import os
from decouple import config
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

app = FastAPI()

os.environ["GOOGLE_API_KEY"] = config("GEMINI_API_KEY", cast=str)

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", stream=True)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{text}")
])
chain = prompt | model | StrOutputParser()

chat_history = []


@app.get("/chat")
async def chat_stream(text: str):
    async def generate():
        chat_history.append(HumanMessage(content=text))

        response = ""
        async for chunk in chain.astream({"chat_history": chat_history[-2:], "text": text}):
            response += chunk
            yield f"data: {chunk}\n\n"

        chat_history.append(AIMessage(content=response))

    return StreamingResponse(generate(), media_type="text/event-stream")