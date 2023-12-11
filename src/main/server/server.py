from fastapi import FastAPI
from ..routes.routes import router
from ..routes.auth_routes import auth_router
from ..routes.web_socket import ws_router

app = FastAPI()

app.include_router(router)
app.include_router(auth_router)
app.include_router(ws_router)
