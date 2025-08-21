from datetime import datetime , timezone
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from websocket_manager import manager
from db.models import NoteDB

from db.database import SessionLocal

scheduler = AsyncIOScheduler()

def schedule_note_job(note_id : int  , runtime : datetime):
    if runtime.tzinfo is None:
        runtime = runtime.replace(tzinfo=timezone.utc)

    scheduler.add_job(
        func=dispatch_reminder,
        trigger="date", 
        run_date = runtime,
        args = [note_id],
        id = f"note-{note_id}",
        replace_existing=True, 
        misfire_grace_time=60 

    )

def dispatch_reminder(note_id : int):
    import asyncio
    asyncio.create_task(_dispatch_async(note_id)) 

async def _dispatch_async(note_id : int):
    with SessionLocal() as db: 
        note = db.get(NoteDB , note_id)
        if note:
            await manager.broadcast(f"REMINDER : {note.id} : {note.title}")