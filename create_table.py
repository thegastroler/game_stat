from datetime import datetime

from sqlalchemy import (Column, Date, Float, Integer, MetaData, Table,
                        create_engine)

DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/postgres"

db = create_engine(DATABASE_URI)

meta = MetaData(db)  
table = Table(
    'statistics', meta,  
    Column('date', Date, primary_key=True),
    Column('views', Integer),
    Column('clicks', Integer),
    Column('cost', Float),
    Column('cpc', Float),
    Column('cpm', Float))

with db.connect() as conn:

    # Create
    table.create()
    insert_statement = table.insert().values(
        date=datetime.now().strftime('%Y-%m-%d'),
        views=1,
        clicks=1,
        cost=1,
        cpc=1,
        cpm=1000
        )
    conn.execute(insert_statement)
