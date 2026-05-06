from dataclasses import dataclass, field

@dataclass
class Usuario:
    id_usuario: int = None
    nome: str = ""
    senha: str = ""

    def __post_init__(self):
        Usuario._next_id = getattr(Usuario, '_next_id', 0) + 1
        self.id_usuario = Usuario._next_id

    def toString(self):
        return f"Usuário {self.id_usuario}: {self.nome}"