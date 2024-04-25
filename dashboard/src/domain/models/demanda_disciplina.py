from ....src.domain.interface.json_serializible import JsonSerializableInterface

class DemandaDisciplina(JsonSerializableInterface):

    def __init__(self, disciplina: str, aluno: str, cursando: bool, atrasado: bool, ano: int) -> None:

        self.disciplina = disciplina
        self.aluno = aluno
        self.cursando = cursando
        self.atrasado = atrasado
        self.ano = ano

    def to_json(self) -> dict:
        return {
            "disciplina": self.disciplina,
            "aluno": self.aluno,
            "cursando": self.cursando,
            "atrasado": self.atrasado,
            "ano": self.ano
        }
    
    def identificador(self) -> str:
        return f'{self.disciplina}/{self.aluno}/{self.ano}'
    