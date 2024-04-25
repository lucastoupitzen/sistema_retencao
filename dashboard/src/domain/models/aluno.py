from ....src.domain.interface.json_serializible import JsonSerializableInterface

class Aluno(JsonSerializableInterface):

    def __init__(self, nro_usp: str, nome: str, ano_ingresso: int) -> None:

        self.nro_usp = nro_usp
        self.nome = nome
        self.ano_ingresso = ano_ingresso

    def to_json(self) -> dict:
        return {
            "nro_usp": self.nro_usp,
            "nome": self.nome,
            "ano_ingresso": self.ano_ingresso
        }
    
    def identificador(self) -> str:
        return self.nro_usp
    
