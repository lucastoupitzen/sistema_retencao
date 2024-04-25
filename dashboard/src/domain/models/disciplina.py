from ....src.domain.interface.json_serializible import JsonSerializableInterface

class Disciplina(JsonSerializableInterface):

    def __init__(self, codigo: str, nome: str, semestre_ideal: int) -> None:

        self.codigo = codigo
        self.nome = nome
        self.semestre_ideal = semestre_ideal

    def to_json(self) -> dict:
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "semestre_ideal": self.semestre_ideal
        }
    
    def identificador(self) -> str:
        return self.codigo
    