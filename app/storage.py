from typing import List, Optional, Tuple

from fastapi import status
from sqlalchemy import desc

from database import Session
from database.model import Statistics
from schemas import StatisticsSchema


class StatisticsStorage:
    def __init__(self, session: Session):
        self.session = session

    def get_statistics(self, d_from: str, d_to: str,
                       order_by: Optional[str] = Statistics.date) \
        -> List[Optional[StatisticsSchema]]:
        with self.session() as session:
            return session.query(Statistics).where(
                Statistics.date.between(d_from, d_to)).order_by(
                    desc(order_by)).all()

    def create_statistics(self, data: List[Optional[StatisticsSchema]]) \
        -> Tuple[str, str, List[Optional[StatisticsSchema]]]:
        with self.session() as session:
            check = session.query(Statistics).where(Statistics.date.in_(
                [i.date for i in data])).all()
            data = [k for k in data[::-1] if k.date not in [
                i.date.strftime('%Y-%m-%d') for i in check]]
            stat = [Statistics(
                date=i.date,
                views=i.views,
                clicks=i.clicks,
                cost=i.cost,
                cpc=None,
                cpm=None
                ) for i in data]
            for i in stat:
                if i.cost and i.clicks:
                    i.cpc = round(float(i.cost / i.clicks), 2)
                if i.cost and i.views:
                    i.cpm = round(float(i.cost / i.views * 1000), 2)
            session.add_all(stat)
            session.commit()
            session.expire_all()
            if not check:
                return status.HTTP_201_CREATED, \
                    'Statistics created successfully', data
            else:
                return (status.HTTP_206_PARTIAL_CONTENT,
                        f'Statistics for dates already exist: \
                        {[str(i.date) for i in check]}', data)

    def delete_statistics(self) -> str:
        with self.session() as session:
            session.query(Statistics).delete()
            session.commit()
            return 'Statistics deleted successfully'
