import os
from decouple import config
from langchain_community.document_loaders import AsyncHtmlLoader

# from latest_user_agents import get_random_user_agent


os.environ.setdefault("GOOGLE_API_KEY", config("GEMINI_API_KEY"))
# os.environ["USER_AGENT"] = get_random_user_agent()

url = "https://en.wikipedia.org/wiki/NoSQL"


loader = AsyncHtmlLoader(
    web_path=url,
)

docs = loader.load()
# print(docs)
# print(docs[0])
# print(docs[0].page_content) # show html
print(docs[0].metadata)