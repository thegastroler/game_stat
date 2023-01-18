from datetime import date
from typing import List, Optional, Union

from pydantic import BaseModel


class StatisticsSchema(BaseModel):
    date: Union[str, date]
    views: Optional[int] = None
    clicks: Optional[int] = None
    cost: Optional[float] = None
    cpc: Optional[float] = None
    cpm: Optional[float] = None

    class Config:
        orm_mode = True


class CreateStatistics(BaseModel):
    body: List[StatisticsSchema]


class GetStatistics(BaseModel):
    date_from: str
    date_to: str
    order_by: Optional[str] = None
