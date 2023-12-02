from fastapi import FastAPI

from mynearestleedsmarginal.views import home

app = FastAPI()

app.include_router(home.router)
