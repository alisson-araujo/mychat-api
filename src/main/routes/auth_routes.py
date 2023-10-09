from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from src.drivers.auth.security import (
    authenticate_user,
    create_access_token,
    get_current_user,
)
from pydantic import BaseModel
from typing import Annotated, Optional
from datetime import timedelta

from src.main.adapters.request_adapter import request_adapter
from src.main.composers.register_user_composer import register_user_composer
from src.errors.error_handler import handle_errors


auth_router = APIRouter()


class Token(BaseModel):
    access_token: str
    token_type: str


@auth_router.post("/token", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    http_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect phone number or password",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        user = authenticate_user(form_data.username, form_data.password)
    except Exception:
        raise http_exception
    if not user:
        raise http_exception

    access_token_expires = timedelta(minutes=60)
    access_token = create_access_token(
        data={"sub": user.phone}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.post("/token/refresh", response_model=Token)
async def refresh_token(current_user: Optional[str] = Depends(get_current_user)):
    access_token_expires = timedelta(minutes=60)
    access_token = create_access_token(
        data={"sub": current_user}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.post("/register-user")
async def register_user(request: Request):
    try:
        http_response = await request_adapter(request, register_user_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return http_response
