from pydantic import BaseModel
from typing import List

class Record(BaseModel):
    key: str
    table: str
    english: str
    languages: List[str]

class TranslateRequest(BaseModel):
    token: str
    records: List[Record] 