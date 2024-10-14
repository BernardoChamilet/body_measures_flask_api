from pydantic import BaseModel, Field

class Usuario(BaseModel):
    usuario: str = Field(..., min_length=7)
    nome: str = Field(..., min_length=2)
    senha: str = Field(..., min_length=6)

class Senhas(BaseModel):
    senha_atual: str = Field(..., min_length=6)
    senha_nova: str = Field(..., min_length=6)