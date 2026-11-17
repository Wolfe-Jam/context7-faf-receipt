from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI
from sqlmodel import Session

from app.db import get_session, init_db
from app.models import Item, ItemCreate, ItemRead


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)
SessionDep = Annotated[Session, Depends(get_session)]


@app.post("/items", response_model=ItemRead)
def create_item(item: ItemCreate, session: SessionDep) -> Item:
    db_item = Item.model_validate(item)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item
