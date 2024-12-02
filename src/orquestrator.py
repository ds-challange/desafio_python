import asyncio

from src.configs.beanie_config import CHUNK_SIZE
from src.modules.airline.contracts.implementations.airline_etl.document_db_insert_from_csv import document_db_insert_from_csv
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
    
    limit_workers = asyncio.Semaphore(3)
    
    async def download_file(file_name):
        async with limit_workers:
            download_is_completed = await get_kaggle_airline_dataset_zip(file_name=file_name)
            if download_is_completed:
                print(f"Download {file_name} finished")
            else:
                print(f"Download {file_name} failed")

    download_tasks = [download_file(file_name) for file_name in list_file_names]
    await asyncio.gather(*download_tasks)
    
    for file_name in list_file_names:
        try:
            unzip_file_path = await unzip_file(
                file_name=file_name,
                file_path=file_path,
                extract_to=extract_to,
                delete_zip=True
            )
            await document_db_insert_from_csv(file_path=unzip_file_path, chunk_size=CHUNK_SIZE)
            
            print(f"Inserção de {file_name} concluída")
        except Exception as e:
            print(f"Erro ao inserir dados: {e}, arquivo: {file_name}")

