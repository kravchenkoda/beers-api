from fastapi import FastAPI

from routers.beers import beers_router
from routers.auth import auth

app = FastAPI()

app.include_router(beers_router)
app.include_router(auth)
