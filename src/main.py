import asyncio

from src.modules.airline.contracts.implementations.airline_etl.parse_csv_to_document import parse_csv_to_document
from src.modules.airline.contracts.implementations.beanie.document import AirlineDocument
from src.orquestrator import get_data
from src.providers.kaggle.get_kaggle_airline_dataset import find_file_names, get_kaggle_airline_dataset_zip
from src.configs.beanie_config import  init_db
from src.utils.unzip_files import unzip_file


if __name__ == "__main__":
    async def main():
        """
        Main function to run the application
        
        """
        try:
            await init_db()
        except Exception as e:
            print(f"Error to init db:{e}")
            
            
        try:
            await get_data()
        except Exception as e:
            print(f"Error to get data:{e}")
        

        
      
        
                
                


asyncio.run(main())