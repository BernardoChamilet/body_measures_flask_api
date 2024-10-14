from pydantic import BaseModel
from datetime import date

# Classe para validação de dados de medidas
class Medida(BaseModel):
    data: date
    peso: float
    ombro: float
    peito: float
    braco: float
    antebraco: float
    cintura: float
    quadril: float
    coxa: float
    panturrilha: float
    
