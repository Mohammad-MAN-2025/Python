from re import S
from turtle import update
from xmlrpc.client import FastMarshaller
from pydantic import BaseModel, ConfigDict, Field 
from typing import List , Optional
from datetime import datetime


class NoteBase(BaseModel):
    title : str = Field(... , min_length=1 , max_length=100)
    content : Optional[str] = None
    remind_at : Optional[datetime] = None
    done : bool = False

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    title : Optional[str] = None
    content : Optional[str] = None
    remind_at : Optional[datetime] = None
    done : Optional[bool] = False


class NoteOut(NoteBase):
    id : int
    created_at  : datetime
    updated_at : datetime

    model_config = ConfigDict(from_attributes=True)
