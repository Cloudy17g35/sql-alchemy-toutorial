from sqlalchemy import text
import sqlalchemy as db
from conn_params import CONNECTION_STRING


engine = db.create_engine(CONNECTION_STRING)


if __name__ == '__main__':
    with engine.connect() as c:
        query = text('select * from main')
        res = c.execute(query).all()
    print(res)