from .....src.domain.models.discipline_demand import DisciplineDemand
from django.db import transaction
from .....src.domain.models.discipline import Discipline
from .....src.data.interfaces.discipline_demand_repository import DisciplineDemandRepositoryInterface
from .student_repository import StudentRepository
from typing import List, Dict
from models import DisciplineDemand as DisciplineDemand_db
from models import Student as Student_db
from models import Discipline as Discipline_db

class DisciplineDemand_Registering_Exception(Exception):
    def __init__(self, message="Discipline demand could not be registered!"):
        self.message = message
        super().__init__(self.message)

class DisciplineDemand_Deleting_Exception(Exception):
    def __init__(self, message="Discipline demand could not be deleted!"):
        self.message = message
        super().__init__(self.message)

class DisciplineDemandRepository(DisciplineDemandRepositoryInterface):

    @classmethod
    def register_demand(cls, demand: DisciplineDemand) -> None: 

        exists = DisciplineDemand_db.objects.filter(
            discipline=demand.discipline,
            student=demand.student,
            year=demand.year
        )
        if not exists:
            new_demand = DisciplineDemand_db.objects.create(
                discipline = demand.discipline,
                student = demand.student,
                currently_studying = demand.currently_studying,
                late = demand.late,
                year = demand.year
            )

            try:
                new_demand.save()
            except DisciplineDemand_Registering_Exception as e:
                print(f"Exception: {e}")

    @classmethod
    def delete_all_demands(cls) -> None: 

        try:
            DisciplineDemand_db.objects.all().delete()
        except DisciplineDemand_Deleting_Exception as e:
            print(f"Exception: {e}")
    
    @classmethod
    def list_late_students(cls) -> Dict: #return a dict with the amount of late subjects of each student

        # all students informations
        students_repo = StudentRepository()
        students = students_repo.list_students()

        response = {}
        for student in students:

            late_disciplines = DisciplineDemand_db.objects.filter(
                student = Student_db.objects.get(nro_usp = student.nro_usp),
                late = True
            )
            response[student.nro_usp] = len(late_disciplines)
        
        return response
    
    @classmethod
    def read_discipline_demand(cls, discipline: str, year: int) -> Dict:

        response = {}
        disc = Discipline_db.objects.get(code = discipline)
        demand = DisciplineDemand_db.objects.filter(
            discipline = disc.code,
            year = year
        )

        response["ideal period"] = disc.ideal_semester
        response["total students"] = len(demand)
        response["students currently studdying"] = 0
        response["students to study - ideal period"] = 0
        response["students to study - late"] = 0

        for case in demand:
            if case.currently_studying: response["students currently studdying"] += 1
            elif case.late:
                response["students to study - late"] += 1
            else:
                response["students to study - ideal period"] += 1
        
        return response

    @classmethod
    @transaction.atomic
    def register_batch_demands(cls, demands: List[Discipline]) -> None: 

        Discipline_db.objects.bulk_create(demands)


    @classmethod
    def existing_demand(self, discipline: str, student: str, year: int) -> bool:

        disc = Discipline_db.objects.get(code = discipline)
        stud = Student_db.objects.get(nro_usp= student)

        exists = DisciplineDemand_db.objects.filter(
            discipline = disc,
            student = stud,
            year = year
        )

        if exists: return True
        return False
    