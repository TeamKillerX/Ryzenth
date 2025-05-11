from pydantic import BaseModel
from typing import Optional

class HybridParams(BaseModel):
    query: str
  
