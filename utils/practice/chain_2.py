import json
import os
from decouple import config
from langchain.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser


os.environ.setdefault("GOOGLE_API_KEY", config("GEMINI_API_KEY"))

model = init_chat_model("gemini-2.0-flash", model_provider="google-genai")

parser = JsonOutputParser()

templates = """
Provide a JSON response explaining {char} from {char_2} with these keys:
- "definition": "clear definition",
- "purpose": "main use cases",
- "example": "code example"

Output ONLY valid JSON like this:
{{
  "definition": "...",
  "purpose": "...",
  "example": "..."
}}

Now explain {char} from {char_2}:
"""

# prompt = PromptTemplate(
#     template=templates,
#     input_variables=['char', "char_2"]
# )
prompt = PromptTemplate(
    template=templates,
    input_variables=['char', "char_2"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

# t_chain = prompt | model
# t_chain = prompt | model | StrOutputParser()
t_chain = prompt | model | parser

res = t_chain.invoke(
    {
        "char": "chain",
        "char_2": "langchain framework",
    }
)
# print(res.content)
# with open("chain.json", "w") as f:
#     f.write(json.dumps(res, indent=4))

