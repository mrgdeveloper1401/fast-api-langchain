import os
from decouple import config

os.environ.setdefault("GOOGLE_API_KEY", config("GEMINI_API_KEY"))

