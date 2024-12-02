

from beanie import Document
from src.modules.airline.contracts.entities.airline import Airline


class AirlineDocument(Document, Airline):
    class Settings:
        name = "airline"
        use_state_management = True