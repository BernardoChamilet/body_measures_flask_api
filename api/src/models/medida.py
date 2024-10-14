from pydantic import BaseModel
from datetime import date

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
    
