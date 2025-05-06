import os
from decouple import config
from langchain_community.document_transformers import Html2TextTransformer
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings

# تنظیم User-Agent
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
os.environ["GOOGLE_API_KEY"] = config("GEMINI_API_KEY")

url = "https://en.wikipedia.org/wiki/NoSQL"

# لود صفحه وب
loader = AsyncHtmlLoader(url)
doc = loader.load()

# تبدیل HTML به متن
html_to_text = Html2TextTransformer().transform_documents(doc)

# تقسیم متن
text_spliter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=20
)
text_chunk = text_spliter.split_documents(html_to_text)

# ایجاد embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=config("GEMINI_API_KEY")
)

# ایجاد و ذخیره vector store
db = FAISS.from_documents(
    documents=text_chunk,
    embedding=embeddings
)

print(f"تعداد اسناد ذخیره شده: {len(db.index_to_docstore_id)}")