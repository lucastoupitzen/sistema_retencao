from typing import Dict
from ....src.data.interfaces.discipline_demand_repository import DisciplineDemandRepositoryInterface
from ....src.domain.use_cases.list_students_subjects import ListStudentsSubjectsInterface

class ListStudentsSubjects(ListStudentsSubjectsInterface):

    def __init__(self, discipline_demand_repo: DisciplineDemandRepositoryInterface) -> None:
        
        self.__discipline_demand_repo = discipline_demand_repo

    def list_students_most_subjects_to_do(self) -> Dict:
        
        response = self.__discipline_demand_repo.list_late_students()

        return response
        