import pandas as pd

from src.modules.airline.contracts.implementations.beanie.document import AirlineDocument


async def parse_csv_to_document (file_path:str) -> list[AirlineDocument]:
    
    """ Parse the csv file to a list of AirlineDocument

    Returns:
        _type_: list[AirlineDocument]: List of AirlineDocument
    """
    
    df = pd.read_csv(file_path, sep=',', encoding='utf-8')
    data = df.to_dict(orient='records')
    documents = [AirlineDocument(**airline) for airline in data] 
    return documents