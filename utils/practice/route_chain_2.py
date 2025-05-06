import os
from decouple import config
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from operator import itemgetter

from langchain_core.runnables import RunnableBranch

# set envfile
os.environ.setdefault("GOOGLE_API_KEY", config("GEMINI_API_KEY"))

# create model
model = init_chat_model("gemini-2.0-flash", model_provider="google-genai")

parser = StrOutputParser()

chain_parser = model | parser

templates = """
just classify the topic of the following question: {question} into onde of these three categories:
['code', 'therapy', 'general'] with just one category without any explanation.
"""

prompt = PromptTemplate(
    template=templates,
    input_variables=['question'],
)

classifier_chain = prompt | chain_parser


# res = classifier_chain.invoke(
#     {
#         "question": "i lost my cousin 3 month ago"
#     }
# )

# print(res)

branch = RunnableBranch(
    (lambda x: "terapy" == x['topic'].lower(), therapist_prompt),
    (lambda x: "code" == x['topic'].lower(), code_developer_prompt),
    general_chain
)

full_chain = (
    {
        "topic": classifier_chain,
        "question": itemgetter("question"),
        "language": lambda x: x.get('topic', None).lower(),
    } | bra
)