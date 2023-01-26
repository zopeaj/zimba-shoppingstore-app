from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
