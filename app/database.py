from typing import Annotated

from fastapi import Depends
from sqlmodel import create_engine,Session
from app.settings import setting

engine=create_engine(setting.DATABASE_URL,connect_args={"check_same_thread":False})

def get_session():
    with Session(engine) as session:
        yield session

SessionDep=Annotated[Session,Depends(get_session)]