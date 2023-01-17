from typing import Optional, TypeVar, Generic
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class StatisticsScema(BaseModel):
    date: str
    views: Optional[int] = None
    clicks: Optional[int] = None
    cost: Optional[float] = None
    cpc: Optional[float] = None
    cpm: Optional[float] = None

    class Config:
        orm_mode = True


class RequestStatistics(BaseModel):
    parameter: StatisticsScema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]