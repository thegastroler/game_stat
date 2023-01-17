from fastapi import FastAPI
import uvicorn
from database import engine, model, Session
from schemas import StatisticsScema
from storage import StatisticsStorage
app = FastAPI()

model.Base.metadata.create_all(bind=engine)


@app.get('/')
def get_statistics():
    return StatisticsStorage(Session).get_statistics()


@app.post('/')
def post_statistics(request: StatisticsScema):
    return StatisticsStorage(Session).create_statistics(data=request)


if __name__ == '__main__':
    uvicorn.run('main:app', log_level="info")