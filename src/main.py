import zipfile
import asyncio
import os

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src.providers.kaggle.get_kaggle_airline_dataset import find_file_names, get_kaggle_airline_dataset_zip
from src.configs.beanie_config import MONGODB_URL, AIRLINE_DOCUMENT_MODELS


extract_to = "temp/unzip/data"
file_path = "temp/data"

async def unzip_file(file_name: str,file_path:str, extract_to: str, delete_zip:bool = True) -> str:
    os.makedirs(extract_to, exist_ok=True)

    zip_file = file_path+"/"+file_name

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        
    if delete_zip:
        os.remove(file_path)
    
    unziped_file_path = extract_to + "/" + file_name
    return unziped_file_path

if __name__ == "__main__":
    async def main():
        airline_database = AsyncIOMotorClient(MONGODB_URL).airline  # type: ignore
        await init_beanie(airline_database, document_models=AIRLINE_DOCUMENT_MODELS)
        
        
        list_file_names = await find_file_names()
        for file_name in list_file_names:
            await_zip_download = [
                get_kaggle_airline_dataset_zip(file_name=file_name)
            ]

        for completed_zip_download in asyncio.as_completed(await_zip_download):
            file_name, download_is_completed = await completed_zip_download
            
            if download_is_completed:
                print(f"Download of {file_name} is completed")
                unziped_file_path = await unzip_file(
                    file_name=file_name,
                    file_path=file_path,
                    extract_to=extract_to,
                    delete_zip=True
                    )
                
                


asyncio.run(main())