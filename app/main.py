from fastapi import FastAPI
from app.models import create_db_and_tables
from app.database import SessionDep


app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"status":"Backend is awake!"}


from app.routers import v1_router
app.include_router(v1_router.v1_router)