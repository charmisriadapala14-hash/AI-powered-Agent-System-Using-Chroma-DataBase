import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

EMBEDDING_MODEL = "text-embedding-3-small"

LLM_MODEL = "gpt-4o-mini"

CHROMA_DB_PATH = "./chroma_db"

COLLECTION_NAME = "agent_documents"

if not OPENAI_API_KEY:
    print("Warning: OPENAI_API_KEY is not configured.")
