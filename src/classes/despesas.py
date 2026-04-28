from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Despesas:
    # Gerando um ID único automaticamente
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    id_categoria: int
    descricao: str = ""
    valor: float
    data_inclusao: datetime = field(default_factory=datetime.now)


    def toString(self):
        return f"Despesa: {self.descricao} - Valor: {self.valor} - Inclusão: {self.data_inclusao}"