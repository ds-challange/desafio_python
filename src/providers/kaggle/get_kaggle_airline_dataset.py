import kaggle

from src.configs.kaggle_config import KAGGLE_DATASET, KAGGLE_OWNER, KAGGLE_URL
from src.providers.kaggle.contracts.dtos.kaggle_dtos import KaggleDownloadFilesDto


async def find_file_names()-> list[str]:
    """
    Find the file names of the kaggle dataset
    """
    
    list_dto_names = []
    datasets_describe_list_files:list[KaggleDownloadFilesDto] = (
        kaggle.api.datasets_list_files(
            owner_slug=KAGGLE_OWNER,
            dataset_slug=KAGGLE_DATASET
            )
        )
    for dataset in datasets_describe_list_files:
        list_dto_names.append(dataset.name)
    return list_dto_names
    
async def get_kaggle_airline_dataset_zip(file_name: str) -> tuple[str, bool]:
    """
    Download the kaggle dataset zip file

    Args:
        file_name (str): The file name of the kaggle dataset

    Returns:
        tuple[str, bool]: The file name and if the download is completed
    """
    
    download_is_completed = (
        kaggle.api.dataset_download_file(
            dataset=KAGGLE_URL,
            path="temp/data",
            file_name=file_name
            )
        )
    return file_name, download_is_completed

