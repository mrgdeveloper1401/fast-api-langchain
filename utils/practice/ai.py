import getpass
import os
from langchain.prompts import PromptTemplate

if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
# print(model.invoke("pep8 in python"))

templates = """
what is {word}
"""

prompt = PromptTemplate(template=templates, input_variables=['word'])

res_1 = prompt.format(word='pep8',)

print(model.invoke(res_1))