from fastapi import APIRouter,WebSocket, WebSocketDisconnect
from schemas import NoteOut , NoteCreate , NoteUpdate 
from websocket_manager import manager

router = APIRouter(prefix = "/ws" , tags = ["ws"])

@router.websocket("/")
async def websocket_endpoint(ws : WebSocket):
    await manager.connect(ws)
    try:
        while True :
            await ws.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(ws)