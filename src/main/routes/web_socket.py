from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Header
from src.drivers.auth.security import get_current_user
from typing import List, Annotated, Optional, Dict


ws_router = APIRouter()

clients: Dict[str, WebSocket] = {}


@ws_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: Optional[str] = Header(None)):
    await websocket.accept()

    user = await get_current_user(token)

    clients[user] = websocket

    try:
        while True:
            data = await websocket.receive_json()
            recipient = data["recipient"]
            data = data["data"]
            print(f"{user} sent: {data} to {recipient}")

            if recipient in clients:
                await clients[recipient].send_text(data)

    except WebSocketDisconnect:
        del clients[user]
        if not clients:
            print("No more clients, closing...")
