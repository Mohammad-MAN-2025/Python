from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import Base , engine
from scheduler import scheduler
from Routers import notes , websocket
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)
    scheduler.start()

    yield  

    scheduler.shutdown(wait=False)

app = FastAPI(title="Notes with SQLAlchemy", lifespan=lifespan)

app = FastAPI(title="Note with SqlAlchemy")
app.include_router(notes.router)

app.include_router(websocket.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"] , allow_credentials = True ,
    allow_methods = ["*"] , allow_headers = ["*"]
)
