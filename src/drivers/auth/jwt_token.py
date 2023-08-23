from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from jose import jwt, JWTError

from src.main.composers.get_user_composer import get_user_composer
from src.main.adapters.request_adapter import request_adapter
from src.errors.error_handler import handle_errors


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class TokenData(BaseModel):
    phone_number: str | None = None


def get_user(phone_number: str):
    class HttpRequest:
        def __init__(self) -> None:
            self.query_params = {"phone_number": phone_number}

    request = HttpRequest()
    try:
        http_response = request_adapter(request, get_user_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return http_response


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, "SECRET_KEY", algorithm="HS256")
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])
        phone_number: str = payload.get("sub")
        if phone_number is None:
            raise credentials_exception
        token_data = TokenData(phone_number=phone_number)
    except JWTError:
        raise credentials_exception
    user = get_user(token_data.phone_number)
    if user is None:
        raise credentials_exception
    return user
