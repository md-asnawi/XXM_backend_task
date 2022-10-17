from pydantic import BaseModel
from typing import Optional

class Dimension(BaseModel):
    height: float
    depth: float
    width: float
    pallet_height: float
    wheel_opening_width: float
    
class Pallet(BaseModel):
    id: str
    display_name: Optional[str]
    description: Optional[str]
    dimensions: Dimension