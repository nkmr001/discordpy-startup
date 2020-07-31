import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from setting import Base
from setting import ENGINE

class Dserver(Base):
    __tablename__ = 'Dserver'
    id = Column('id', Integer, primary_key = True)
    name = Column('name', String)

def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)
