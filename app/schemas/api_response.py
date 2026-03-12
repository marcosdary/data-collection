from pydantic import BaseModel
from typing import TypeVar, Generic

T = TypeVar("T")
E = TypeVar("E")

class ApiResponseModel(BaseModel, Generic[T, E]):
    success: bool
    data: T | None = None
    error: E | None = None
    
