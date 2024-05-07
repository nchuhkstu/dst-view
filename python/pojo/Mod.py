from sqlalchemy import Column, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Mod(Base):
    __tablename__ = 'mods'

    mod_id = Column(Text, primary_key=True)
    mod_title = Column(Text)
    mod_author = Column(Text)
    mod_description = Column(Text)
    mod_size = Column(Text)
    mod_push_time = Column(Text)
    mod_update_time = Column(Text)

    def __init__(self, mod_id, mod_title, mod_author, mod_description, mod_size, mod_push_time, mod_update_time):
        self.mod_id = mod_id
        self.mod_title = mod_title
        self.mod_author = mod_author
        self.mod_description = mod_description
        self.mod_size = mod_size
        self.mod_push_time = mod_push_time
        self.mod_update_time = mod_update_time
