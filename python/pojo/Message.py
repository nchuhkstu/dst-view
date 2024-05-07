from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Message(Base):
    __tablename__ = 'message'

    message_id = Column(Integer, primary_key=True)
    message_text = Column(Text)
    message_time = Column(Text)
    message_type = Column(Text)

    def __init__(self, message_text, message_time, message_type):
        self.message_text = message_text
        self.message_time = message_time
        self.message_type = message_type

