from pydantic import BaseModel, Field
from typing import List

class DocumentSummary(BaseModel):
    summary: List[str] = Field(..., title="Summary of the document")