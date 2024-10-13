from pydantic import BaseModel

class Medida(BaseModel):
    data: str
    peso: float
    ombro: float
    peito: float
    braco: float
    antebraco: float
    cintura: float
    quadril: float
    coxa: float
    panturrilha: float
    
