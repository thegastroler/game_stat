from datetime import datetime
from typing import List, Optional

import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from database import Session, engine, model
from schemas import CreateStatistics, GetStatistics, StatisticsSchema
from storage import StatisticsStorage

app = FastAPI()

model.Base.metadata.create_all(bind=engine)


@app.get('/')
def get_statistics(request: GetStatistics) -> List[Optional[StatisticsSchema]]:
    try:
        for i in (request.date_from, request.date_to):
            datetime.strptime(i, '%Y-%m-%d')
    except ValueError:
        return JSONResponse(
            content={"message": f"Incorrect data format in {i}, \
                should be YYYY-MM-DD"})
    return StatisticsStorage(Session).get_statistics(
        d_from=request.date_from,
        d_to=request.date_to,
        order_by=request.order_by
    )


@app.post('/')
def post_statistics(request: CreateStatistics) -> JSONResponse:
    try:
        for i in request.body:
            datetime.strptime(i.date, '%Y-%m-%d')
    except ValueError:
        return JSONResponse(
            content={"message": f"Incorrect data format in '{i.date}', \
                should be YYYY-MM-DD"})
    code, message, result = StatisticsStorage(Session).create_statistics(
        data=request.body)
    return JSONResponse(
        content={
            "message": message,
            "result": [i.dict(exclude_none=True) for i in result]},
        status_code=code)


@app.delete('/')
def delete_statistics() -> JSONResponse:
    message = StatisticsStorage(Session).delete_statistics()
    return JSONResponse(content={"message": message})


if __name__ == '__main__':
    uvicorn.run('main:app', log_level="info")
