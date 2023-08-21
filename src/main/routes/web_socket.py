from fastapi import APIRouter, WebSocket, WebSocketDisconnect


router = APIRouter()

conversation_websockets = []


@router.websocket("/ws")
async def websocket_endpoint(user_id: int, conversation_id: int, websocket: WebSocket):
    await websocket.accept()

    if websocket not in conversation_websockets:
        conversation_websockets.append(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            for ws in conversation_websockets:
                await ws.send_text(data)
    except WebSocketDisconnect:
        conversation_websockets.remove(websocket)
        # await websocket.close()
