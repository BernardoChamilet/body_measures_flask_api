from pydantic import BaseModel

class Usuario(BaseModel):
    usuario: str
    nome: str
    senha: str