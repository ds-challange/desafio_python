
import os
import zipfile

async def unzip_file(file_name: str,file_path:str, extract_to: str, delete_zip:bool = True) -> str:
    """Unzip a file to a specific path

    Args:
        file_name (str): File name to unzip
        file_path (str): File path to unzip
        extract_to (str): Extract to path where the file will be unzip
        delete_zip (bool, optional): Boolean to delete zip after extract. Defaults to True.

    Returns:
        str: Path of the unzip file
    """
    
    os.makedirs(extract_to, exist_ok=True)

    zip_file = file_path+"/"+file_name+".zip"

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        
    if delete_zip:
        os.remove(zip_file)
    
    unzip_file_path = extract_to + "/" + file_name
    return unzip_file_path



    
