import os
from dotenv import load_dotenv

load_dotenv()  # This loads variables from .env into environment

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if GROQ_API_KEY is None:
    raise ValueError("API key not found. Make sure .env is set up correctly.")


DATABASE_PATH = "data/memories.db"
USER_NAME = "Boss"
