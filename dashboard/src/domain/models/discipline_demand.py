from ..interface.json_serializible import JsonSerializableInterface

class DisciplineDemand(JsonSerializableInterface):

    def __init__(self, discipline: str, student: str, currently_studying: bool, late: bool, year: int) -> None:

        self.discipline = discipline
        self.student = student
        self.currently_studying = currently_studying
        self.late = late
        self.year = year

    def to_json(self) -> dict:
        return {
            "disciplina": self.discipline,
            "aluno": self.student,
            "cursando": self.currently_studying,
            "atrasado": self.late,
            "ano": self.year
        }
    
    def identifier(self) -> str:
        return f'{self.discipline}/{self.student}/{self.year}'
    