from dataclasses import dataclass, field

@dataclass
class Categoria:
    id_categoria: int = field(init=False)
    nome: str = ""
    descricao: str = ""
    
    def __post_init__(self):
        Categoria._next_id = getattr(Categoria, '_next_id', 0) + 1
        self.id_categoria = Categoria._next_id

    def toString(self):
        return f"Categoria: {self.descricao}"