from datetime import datetime, timezone
from typing import  List
from db.database import get_db
from db.models import NoteDB
from scheduler import scheduler , schedule_note_job
from fastapi import APIRouter, HTTPException, Depends , status
from sqlalchemy.orm import Session
from schemas import NoteOut , NoteCreate , NoteUpdate 


def to_utc(dt , assume_tz = timezone.utc):
    if dt is None :
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo = assume_tz)
    return dt.astimezone(timezone.utc)


router = APIRouter(prefix="/notes" , tags=["notes"])

@router.post("/" , response_model = NoteOut)
def create_note(note : NoteCreate , db : Session = Depends(get_db)):
    db_note = NoteDB(
        title = note.title , 
        content = note.content,
        remind_at = to_utc(note.remind_at) , 
        done = note.done
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    if db_note.remind_at and to_utc(db_note.remind_at) > datetime.now(timezone.utc):
        schedule_note_job(note_id=db_note.id ,runtime=db_note.remind_at )
    return db_note

@router.get("/" , response_model = List[NoteOut])
def list_notes(db:Session = Depends(get_db)):
    return db.query(NoteDB).order_by(NoteDB.created_at.desc()).all()
    

@router.get("/{note_id}" , response_model = NoteOut)
def get_note(note_id : int , db : Session = Depends(get_db)):
    note = db.get(NoteDB , note_id)
    if not note :
        raise HTTPException(404 ,"Not Found!")
    return note


@router.patch("/{note_id}" , response_model = NoteOut)
def update_note(note_id : int , data : NoteUpdate , db : Session = Depends(get_db)):
    note = db.get(NoteDB , note_id)
    if not note : 
        raise HTTPException(404 , "Not Found!")
    for key , value in data.model_dump(exclude_unset=True).items():
        setattr(note , key , value)
    db.add(note)
    db.commit()
    db.refresh(note)
    if note.remind_at and to_utc(note.remind_at) > datetime.now(timezone.utc):
        schedule_note_job(note_id=note.id , runtime=to_utc(note.remind_at))
    return note


@router.delete("/{note_id}" , status_code = status.HTTP_204_NO_CONTENT)
def delete_note(note_id : int , db : Session = Depends(get_db)):
    note = db.get(NoteDB , note_id)
    if not note :
        raise HTTPException(404 , "Not Found!")
    db.delete(note)
    db.commit()
    try:
        scheduler.remove_job(f"not--{note_id}")
    except:
        pass


