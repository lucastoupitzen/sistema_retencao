import os
import tqdm
from typing import Dict
from ....src.domain.use_cases.upload_retention_sheet import UploadRetentionSheetInterface
from ....src.data.interfaces.student_repository import StudentRepositoryInterface
from ....src.data.interfaces.discipline_demand_repository import DisciplineDemandRepositoryInterface
from ....src.data.interfaces.discipline_repository import DisciplineRepositoryInterface
from ....src.domain.models.student import Student
from ....src.domain.models.discipline_demand import DisciplineDemand
from ....utilitarios.Planilha import Planilha


class UploadRetentionSheet(UploadRetentionSheetInterface):

    def __init__(self, student_repo: StudentRepositoryInterface, 
                 discipline_demand_repo: DisciplineDemandRepositoryInterface,
                 discipline_repo: DisciplineRepositoryInterface) -> None:
        
        self.__student_repo = student_repo
        self.__discipline_demand_repo = discipline_demand_repo
        self.__discipline_repo = discipline_repo

    def upload_sheet(self, path: str, year: int) -> Dict:
        
        #finding the file
        file = os.path.abspath(f"dashboard/{path}")
        # making sure this data isn't already registered

        #working with the xls file using pandas
        sheet = Planilha(file)

        disciplines = self.__discipline_repo.list_all_disciplines()

        for discipline in disciplines:

            student_objects = []
            demand_objects = []

            data = sheet.get_arquivo_materia(discipline.code)
            print("Loading subject " + discipline.code)

            for index, line in tqdm(data.iloc[1:].iterrows(), total= len(data) - 1, unit='line'):
                student = Student(
                    num_usp= line["Número USP"], 
                    name= line["Nome do Aluno"],
                    start_year= line["Data de ingresso"]
                )
                if not self.__student_repo.existing_student(student_id=student.num_usp):
                    student_objects.append(student) 
                demand = DisciplineDemand(
                    discipline= discipline.code,
                    student= line["Número USP"],
                    currently_studying= line["Cursando?"],
                    year=year
                )
                if not self.__discipline_demand_repo.existing_demand(discipline= discipline.code,
                                                                     student=line["Número USP"],
                                                                     year = year):
                    demand_objects.append(demand)

            self.__student_repo.register_batch_students(student_objects)
            self.__discipline_demand_repo.register_batch_demands(demand_objects)

            print(discipline.code + " loading succeed!")
