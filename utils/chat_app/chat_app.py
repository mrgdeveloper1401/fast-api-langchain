import os
from decouple import config
from langchain.chat_models import init_chat_model
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import SystemMessage, HumanMessage, AIMessage, StrOutputParser


os.environ.setdefault("GOOGLE_API_KEY", config("GEMINI_API_KEY"))


model = init_chat_model(
    "gemini-2.0-flash",
    model_provider="google_genai",
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system", "you are helpful assistance"
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{text}")
    ]
)

chain = prompt | model | StrOutputParser()

chat_history = []

text = [
    "iam an backend developer, with by framework django and fast api",
    "what is my experience?"
]

chat_history = chat_history[-2:]

response_message = chain.invoke(
    {
        "chat_history": chat_history,
        "text": text[0]
    }
)

chat_history.extend(
    [
        HumanMessage(content=text), AIMessage(content=response_message)
    ]
)
