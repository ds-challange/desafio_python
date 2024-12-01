import asyncio

from src.modules.airline.contracts.implementations.airline_etl.parse_csv_to_document import parse_csv_to_document
from src.modules.airline.contracts.implementations.beanie.document import AirlineDocument
from src.providers.kaggle.get_kaggle_airline_dataset import find_file_names, get_kaggle_airline_dataset_zip
from src.utils.unzip_files import unzip_file


async def get_data():
    
    """
    Get the data from Kaggle and insert it to the mongodb database 
    """
    
    extract_to = "temp/unzip/data"
    file_path = "temp/data"
    
    list_file_names = await find_file_names()
    for file_name in list_file_names:
        await_zip_download = [
            get_kaggle_airline_dataset_zip(file_name=file_name)
        ]

    for completed_zip_download in asyncio.as_completed(await_zip_download):
        file_name, download_is_completed = await completed_zip_download
        
        if download_is_completed:
            print(f"Download of {file_name} is completed")
            unzip_file_path = await unzip_file(
                file_name=file_name,
                file_path=file_path,
                extract_to=extract_to,
                delete_zip=True
                )
            
            airline_document:list[AirlineDocument]=(
                parse_csv_to_document(file_path=unzip_file_path)
            )
            await AirlineDocument.insert_many(airline_document)
            
            print(f"Insertion of {file_name} is completed")
            
    print("All files are inserted to the database")