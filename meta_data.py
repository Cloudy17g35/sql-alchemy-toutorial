import sqlalchemy as db
from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String
from conn_params import CONNECTION_STRING


engine = db.create_engine(CONNECTION_STRING)

metadata = MetaData()


user_table = Table(
    "user",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_name', String(50), nullable=False),
    Column('fullname', String(100))
)

address_table = Table(
    'address',
    metadata,
    Column('address', String, nullable=False)
)


if __name__ == '__main__':

    with engine.begin() as conn:
        metadata.create_all(conn)
    with engine.begin() as conn:
        conn.execute(
        user_table.insert( 
            {'id': 1,
            'user_name': 'Jacek'}
        )
        )


