

from pydantic import BaseModel


class KaggleDownloadFilesDto(BaseModel):
        datasetRefNullable: str | None = None
        ownerRefNullable: str | None = None
        nameNullable: str | None = None
        descriptionNullable: str | None = None
        fileTypeNullable: str | None = None
        urlNullable: str | None = None
        ref: str = ''
        datasetRef: str = ''
        hasDatasetRef: bool = False
        ownerRef: str = ''
        hasOwnerRef: bool = False
        name: str = ''
        hasName: bool = True
        creationDate: str = ''
        description: str = ''
        hasDescription: bool = False
        fileType: str = ''
        hasFileType: bool = False
        url: str = ''
        hasUrl: bool = False
        totalBytes: int = 0
        columns: list = []
        