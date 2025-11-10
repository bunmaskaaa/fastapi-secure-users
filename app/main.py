from __future__ import annotations
from fastapi import FastAPI
from .db import Base, engine
from .routers import users

app = FastAPI(title="Secure Users API")
Base.metadata.create_all(bind=engine)

app.include_router(users.router)

@app.get("/")
def root():
    return {"status": "ok"}