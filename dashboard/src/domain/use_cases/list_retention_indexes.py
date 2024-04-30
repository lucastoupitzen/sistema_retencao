from typing import Dict
from abc import ABC, abstractmethod
from ..models.discipline_demand import DemandaDisciplina

class ListRetentionIndexesInterface(ABC):

    @abstractmethod
    def list_retention_indexes_odd(self, year: int) -> Dict: pass

    @abstractmethod
    def list_retention_indexes_even(self, year: int) -> Dict: pass
    