from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List


ws_router = APIRouter()

clients: List[WebSocket] = []


@ws_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    clients.append(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            print(data)
            for client in clients:
                if client != websocket:
                    await client.send_text(data)

    except WebSocketDisconnect:
        clients.remove(websocket)
        if not clients:
            print("No more clients, closing...")
