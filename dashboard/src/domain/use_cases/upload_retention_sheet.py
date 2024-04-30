from abc import ABC, abstractmethod

class UploadRetentionSheetInterface(ABC):

    @abstractmethod
    def upload_sheet(self, path: str, year: int) -> None: pass
