from datetime import datetime
from main import listar_clientes
from pydantic import BaseModel

class factura (BaseModel):
    id : listar_clientes
    fecha : datetime
    total : int
    cliente : str  | None