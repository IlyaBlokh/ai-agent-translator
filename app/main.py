from fastapi import FastAPI
from .api import router

app = FastAPI(title="CSV Translation API")
app.include_router(router)