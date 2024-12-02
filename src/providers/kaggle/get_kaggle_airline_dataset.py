import asyncio
import kaggle

from src.configs.kaggle_config import KAGGLE_DATASET, KAGGLE_OWNER, KAGGLE_URL
from src.providers.kaggle.contracts.dtos.kaggle_dtos import KaggleDownloadFilesDto


async def find_file_names()-> list[str]:
    """
    Find the file names of the kaggle dataset
    """
    
    datasets_describe_list_files:list[KaggleDownloadFilesDto] = (
        kaggle.api.datasets_list_files(
            owner_slug=KAGGLE_OWNER,
            dataset_slug=KAGGLE_DATASET
            )
        )

    dataset_files = datasets_describe_list_files.get('datasetFiles', [])
    typed_files: list[KaggleDownloadFilesDto] = [KaggleDownloadFilesDto(**file) for file in dataset_files]

    file_names = [file.name for file in typed_files]

    return file_names
    
async def get_kaggle_airline_dataset_zip(file_name: str) -> tuple[str, bool]:
    """
    Download the kaggle dataset zip file

    Args:
        file_name (str): The file name of the kaggle dataset

    Returns:
        tuple[str, bool]: The file name and if the download is completed
    """
    
    print(f"Downloading {file_name} await...")
    download_is_completed = (
        kaggle.api.dataset_download_file(
            dataset=KAGGLE_URL,
            path="/code/temp/data",
            file_name=file_name
            )
        )
    if download_is_completed:
        return file_name, download_is_completed

asyncio.run(get_kaggle_airline_dataset_zip("2009.csv"))