import os
from decouple import config
from langchain_community.document_loaders import UnstructuredPDFLoader
from pathlib import Path
from langchain_community.vectorstores import FAISS
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings


BASE_DIR = Path(__file__).resolve().parent

os.environ.setdefault("GOOGLE_API_KEY", config("GEMINI_API_KEY"))

embeddings = GoogleGenerativeAIEmbeddings(
    google_api_key=config("GOOGLE_API_KEY"),
    model="models/gemini-embedding-exp-03-07"
)

loader = UnstructuredPDFLoader(
    file_path=BASE_DIR / "attention.pdf"
)

doc = loader.load()

# print(len(doc))
# print(doc[0].metadata)


vs = FAISS.from_documents(
    embedding=embeddings,
    documents=doc,
)

# print(vs.similarity_search("Decoder"))
