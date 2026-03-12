from pydantic import BaseModel

class ApiErrorModel(BaseModel):
    errorName: str
    typeError: str
    statusCode: int | None = None

