from fastapi import FastAPI, Depends

from routers.beers import beers_router
from dependencies.db import get_db

app = FastAPI(dependencies=[Depends(get_db)])

app.include_router(beers_router)
