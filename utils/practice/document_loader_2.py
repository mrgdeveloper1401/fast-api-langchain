import os
from decouple import config
from langchain_community.document_transformers import Html2TextTransformer
from langchain_community.document_loaders import AsyncHtmlLoader


os.environ.setdefault("GOOGLE_API_KEY", config("GEMINI_API_KEY"))

url = "https://en.wikipedia.org/wiki/NoSQL"

loader = AsyncHtmlLoader(url)

doc = loader.load()

# print(doc)

html_to_text = Html2TextTransformer().transform_documents(doc)
# print(html_to_text[0].page_content)
# print(len(html_to_text[0].page_content))

