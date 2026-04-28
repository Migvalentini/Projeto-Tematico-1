from dataclasses import dataclass

@dataclass
class Categoria:
    id: int = 0
    nome: str = ""
    descricao: str = ""


    def toString(self):
        return f"Categoria: {self.descricao}"