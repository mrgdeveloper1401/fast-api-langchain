import os
from decouple import config
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableBranch


# set envfile
os.environ.setdefault("GOOGLE_API_KEY", config("GEMINI_API_KEY"))

# create model
model = init_chat_model("gemini-2.0-flash", model_provider="google-genai")

# show output
parser = StrOutputParser()

# chain
chain_parser = model | parser

# create prompt
therapist_prompt = PromptTemplate(
    template="you are helpfully therapies please answer {question}",
    input_variables=['question'],
)

# chain
g_chain = therapist_prompt | chain_parser

# prompt
code_developer_prompt = PromptTemplate(
    template="you are excellent language {language} developer, please answer {question}",
    input_variables=['language', "question"],
)

# chain
code_developer_chain = code_developer_prompt | chain_parser

# general chain
general_chain = (
    PromptTemplate.from_template(
        """
        Respond to the following question: {question} answer:
        """
    ) | chain_parser
)

branch = RunnableBranch(
    (lambda x: "terapy" == x['topic'].lower(), therapist_prompt),
    (lambda x: "code" == x['topic'].lower(), code_developer_prompt),
    general_chain
)

full_chain = {
    "topic": lambda x: x['topic'],
    "question": lambda x: x['question'],
    "language": lambda x: x.get('language', None),
} | branch

res = full_chain.invoke(
    {
        "topic": "code",
        "question": "python",
        "language": "python",
    }
)
print(res)
