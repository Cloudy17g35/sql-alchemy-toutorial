from curses import meta
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
import conn_params
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import registry

mapper_registry = registry()
Base = declarative_base()

@mapper_registry.mapped
class User:
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name,
            self.fullname,
            self.nickname,
        )

if __name__ == '__main__':
    print(User.__tablename__)
    # engine  = db.create_engine(
    #     url=conn_params.CONNECTION_STRING
    # )
    # Session = sessionmaker(
    #     bind=engine
    # )
    # with Session.begin() as session:
    #     session.add_all(
    #         [User(
    #     name='Ksawery',
    #     fullname='Lejczak',
    #     nickname='KL')]
    #     )
