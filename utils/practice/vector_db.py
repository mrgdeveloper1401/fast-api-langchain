import os
from decouple import config
from langchain.chat_models import init_chat_model
from langchain_community.vectorstores import FAISS
import google.generativeai as genai
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings

API_KEY = os.environ.setdefault("GOOGLE_API_KEY", config("GEMINI_API_KEY"))
# os.environ.setdefault("GOOGLE_API_KEY", config("GEMINI_API_KEY"))

# genai.configure(api_key=API_KEY)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=API_KEY)

# model = "models/embedding-001"

text = [
    """
    "Structured storage" redirects here. For the Microsoft technology, see COM Structured Storage.
    NoSQL (originally meaning "non-SQL" or "non-relational")[1] refers to a type of database design that stores and retrieves data differently from the traditional table-based structure of relational databases. Unlike relational databases, which organize data into rows and columns like a spreadsheet, NoSQL databases use a single data structure—such as key–value pairs, wide columns, graphs, or documents—to hold information. Since this non-relational design does not require a fixed schema, it scales easily to manage large, often unstructured datasets.[2] NoSQL systems are sometimes called "Not only SQL" because they can support SQL-like query languages or work alongside SQL databases in polyglot-persistent setups, where multiple database types are combined.[3][4] Non-relational databases date back to the late 1960s, but the term "NoSQL" emerged in the early 2000s, spurred by the needs of Web 2.0 companies like social media platforms.[5][6]
    NoSQL databases are popular in big data and real-time web applications due to their simple design, ability to scale across clusters of machines (called horizontal scaling), and precise control over data availability.[7][8] These structures can speed up certain tasks and are often considered more adaptable than fixed database tables.[9] However, many NoSQL systems prioritize speed and availability over strict consistency (per the CAP theorem), using eventual consistency—where updates reach all nodes eventually, typically within milliseconds, but may cause brief delays in accessing the latest data, known as stale reads.[10] While most lack full ACID transaction support, some, like MongoDB, include it as a key feature.[11]
    """
]

# res = genai.embed_content(model, text)
# print(res)

db = FAISS.from_texts(
    texts=text,
    embedding=embeddings
)

res = db.similarity_search(
    "sql",
    k=1
)
print(res)