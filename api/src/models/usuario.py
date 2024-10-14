from pydantic import BaseModel, Field

class Usuario(BaseModel):
    usuario: str = Field(..., min_length=7)
    nome: str = Field(..., min_length=2)
    senha: str = Field(..., min_length=6)