from fastapi import FastAPI
from pydantic import BaseSettings
from dotenv import load_dotenv


class Settings(BaseSettings):
    DATABASE_URL: str
    ECHO_SQL: bool

load_dotenv()
settings = Settings()


from .store import session

app = FastAPI(
    title="Mountain Peaks",
    description="Assessement for 'Python lead dev' job - MFI",
    version="1.0.0",
    contact={
        "name": "Mohamed Ben Thabet",
        "email": "mohamed.ben.thabet.teams@outlook.com"
    },
    openapi_url="/api/openapi.json",
    docs_url="/swagger"
)

from .endpoint import post_peak, get_peak, put_peak, delete_peak, retrieve_peak
