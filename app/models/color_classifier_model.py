from pydantic import BaseModel

class ClassificationResult(BaseModel):
    predicted_class: str
    probabilities: list[int]
