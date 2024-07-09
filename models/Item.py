from pydantic import BaseModel
from typing import Any

class Item(BaseModel):
    key: str
    value: Any
