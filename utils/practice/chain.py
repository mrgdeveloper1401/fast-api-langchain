import os
from decouple import config
from langchain.chains import LLMMathChain
from langchain.chat_models import init_chat_model
from langchain.prompts import PromptTemplate

os.environ.setdefault("GOOGLE_API_KEY", config("GEMINI_API_KEY"))

prompt = PromptTemplate.from_template(
    "what is the best name for a company that makes {product}"
)

model = init_chat_model("gemini-2.0-flash", model_provider="google-genai")

llm_math = LLMMathChain.from_llm(model, verbose=True)

# with open("chain.txt", "w") as f:
#     f.write(llm_math.prompt.template)

i = 0
math_problem = [
    "what is 13 power .34?"
]

print(llm_math.invoke(math_problem[i]))