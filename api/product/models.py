from pydantic import BaseModel
from typing import Optional

class ProductModel(BaseModel):
    pattern_id:  Optional[str] = None
    pattern_Name: str
    pattern_Price: float

class ProductModel2(BaseModel):
    spare_id: Optional[str] = None
    spare_name: str
    spare_Price: float
