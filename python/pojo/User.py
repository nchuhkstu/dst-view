from sqlalchemy import Column, Integer, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    username = Column(Text)
    kleiname = Column(Text)
    role = Column(Text)
    survival_day = Column(Integer)
    survival_second = Column(Integer)
    live = Column(Boolean, default=True)

    def __init__(self, username, kleiname):
        self.username = username
        self.kleiname = kleiname
        self.survival_day = 0
        self.survival_second = 0
        self.live = True
        self.role = "default"

