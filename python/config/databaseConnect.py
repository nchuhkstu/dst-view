from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:Aa13657998660@localhost/dst')
Session = sessionmaker(bind=engine)
