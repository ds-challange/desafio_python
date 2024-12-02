import asyncio

from src.orquestrator import get_data
from src.configs.beanie_config import  init_db


if __name__ == "__main__":
    async def main():
        """
        Main function to run the application
        
        """
        try:
           db_connection = await init_db()
        except Exception as e:
            print(f"Error to init db:{e}")
            
        if db_connection:
            try:
                await get_data()
            except Exception as e:
                print(f"Error to get data:{e}")
                

asyncio.run(main())