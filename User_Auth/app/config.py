import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    MAX_CONCURRENT_LLM_CALLS: int = 5

settings = Settings()