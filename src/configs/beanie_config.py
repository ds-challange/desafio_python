import os
from typing import Any

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from src.modules.airline.contracts.implementations.beanie.document import AirlineDocument



AIRLINE_DOCUMENT_MODELS: list[Any] = [
    AirlineDocument
]   


MONGODB_URL = os.getenv("MONGODB_URL")
CHUNK_SIZE = os.getenv("CHUNK_SIZE") or 10000

async def init_db()-> bool:
    """
    Initialize the database connection
    """
    
    airline_database = AsyncIOMotorClient(MONGODB_URL).airline  # type: ignore
    await init_beanie(airline_database, document_models=AIRLINE_DOCUMENT_MODELS)
    
    return True