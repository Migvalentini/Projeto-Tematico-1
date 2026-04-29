from dataclasses import dataclass, field
from datetime import datetime
@dataclass
class Rendas:
    id_rendas: int = field(init=False)
    id_usuario: str = ""
    descricao: str = ""
    valor: float = None
    data_inclusao: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        Rendas._next_id = getattr(Rendas, '_next_id', 0) + 1
        self.id_rendas = Rendas._next_id

    def toString(self):
        return f"Renda: {self.descricao} - Valor: {self.valor} - Inclusão: {self.data_inclusao}"