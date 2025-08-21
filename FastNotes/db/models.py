from datetime import datetime, timezone
from db.database import Base
from sqlalchemy import  Column, Integer, String, DateTime, Boolean

class NoteDB(Base):
    __tablename__ = "notes"


    id = Column(Integer , primary_key= True , index = True)
    title = Column(String , nullable=False)
    content = Column(String , nullable=True)
    remind_at = Column(DateTime , nullable=True)
    created_at = Column(DateTime , default =lambda : datetime.now(timezone.utc))
    updated_at = Column(DateTime , default=lambda : datetime.now(timezone.utc) , onupdate= lambda : datetime.now(timezone.utc))
    done = Column(Boolean , default=False)