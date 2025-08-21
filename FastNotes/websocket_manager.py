from typing import List
from fastapi import WebSocket


class ConnectionManager():
    def __init__(self):
        self.active : List[WebSocket] = []

    async def connect(self , websocket : WebSocket):
        await websocket.accept()
        self.active.append(websocket)

    def disconnect(self , websocket : WebSocket):
        if websocket in self.active:
            self.active.remove(websocket)
    async def broadcast(self , message : str):
        for ws in self.active:
            try : 
                await ws.send_text(message)
            except:
                self.disconnect(ws)

manager = ConnectionManager()