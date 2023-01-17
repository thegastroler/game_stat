from database.model import Statistics
from schemas import StatisticsScema
from database import Session
from sqlalchemy.future import select


class StatisticsStorage:
    def __init__(self, session: Session):
        self.session = session

    def get_statistics(self):
        with self.session() as session:
            return session.query(Statistics).all()

    def create_statistics(self, data: StatisticsScema):
        stat = Statistics(
            date=data.date,
            views=data.views,
            clicks=data.clicks,
            cost=data.cost,
            cpc=data.cpc,
            cpm=data.cpm
        )
        with self.session() as session:
            session.add(stat)
            session.commit()
            session.refresh(stat)
            return stat
