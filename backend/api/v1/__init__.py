from fastapi import APIRouter
from .endpoints import login, movies, users


v1 = APIRouter(prefix="/v1")

v1.include_router(login)
v1.include_router(movies)
v1.include_router(users)
