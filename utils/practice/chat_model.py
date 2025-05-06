import os
from langchain.chat_models import init_chat_model
from langchain.schema import SystemMessage
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai.chat_models import ChatGeneration
from decouple import config

os.environ.setdefault("GOOGLE_API_KEY", config("GEMINI_API_KEY"))


model = init_chat_model("gemini-2.0-flash", model_provider="google-genai")

debugger = SystemMessage(
    content="i am provide code og python, you debug this code"
)

general = SystemMessage(
    content="please answer question by honestly."
)

prompt = ChatPromptTemplate(
    [
        ("system", "")
    ]
)
