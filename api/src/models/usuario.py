from pydantic import BaseModel, Field

# Classe para validação de dados de usuário 
class Usuario(BaseModel):
    usuario: str = Field(..., min_length=7)
    nome: str = Field(..., min_length=2)
    senha: str = Field(..., min_length=6)

# Classe para validação de dados de atualização de senha
class Senhas(BaseModel):
    senha_atual: str = Field(..., min_length=6)
    senha_nova: str = Field(..., min_length=6)

# Classe para validação de campos no login
class Login(BaseModel):
    usuario: str
    senha: str