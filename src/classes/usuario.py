from dataclasses import dataclass, field
import uuid

@dataclass
class Usuario:
    # Gerando um ID único automaticamente
    id_usuario: str = field(default_factory=lambda: str(uuid.uuid4()))
    username: str = ""
    senha: str = ""

    def toString(self):
        return f"Usuário: {self.username}"