import os
import getpass
from langchain.prompts import PromptTemplate
from langchain.chat_models import init_chat_model


if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("enter API key for Google Gemini: ")


model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

templates = """
{text} {text_2}
"""

prompt = PromptTemplate(template=templates, input_variables=["text", "text_2"])

res_1 = prompt.format(text="what is", text_2="js")

print(model.batch([res_1]))