from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Despesas:
    id_pessoa: int = field(init=False)
    id_categoria: int = None
    id_usuario: str = ""
    descricao: str = ""
    valor: float = None
    data_inclusao: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        Despesas._next_id = getattr(Despesas, '_next_id', 0) + 1
        self.id_rendas = Despesas._next_id

    def toString(self):
        return f"Despesa: {self.descricao} - Valor: {self.valor} - Inclusão: {self.data_inclusao}"