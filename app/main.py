from fastapi import FastAPI
from .api import router

app = FastAPI(title="Translation API")
app.include_router(router)