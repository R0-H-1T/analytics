from typing import List
from pydantic import BaseModel



class Answer(BaseModel):
    mcq: bool
    choice: int | None = None
    text: str | None = None


class Question(BaseModel):
    correct: int | None = None
    mcq: bool
    qna_id: int
    id: int
    text: str | None = None



class QnAnswers(BaseModel):
    qna: List[Question]
    ans: List[List[Answer]]