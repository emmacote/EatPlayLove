from sqlalchemy import Table, Column, Integer, String, create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = "sqlite:///datastore.db"
eng = create_engine(db_url)
Base = declarative_base(bind=eng)


class Food(Base):
    __tablename__ = "foods"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

Session = sessionmaker(bind=eng)
Base.metadata.create_all(eng)

if __name__ == '__main__':
    print("main of model.py executed.")