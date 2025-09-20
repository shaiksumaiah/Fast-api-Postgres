# main.py
import time
from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

import models, schemas, crud
from database import get_db, engine, Base

app = FastAPI(title="FastAPI + Postgres CRUD")

@app.on_event("startup")
def create_tables():
    # retry loop so app waits shortly for Postgres in docker-compose
    retries = 12
    for attempt in range(retries):
        try:
            Base.metadata.create_all(bind=engine)
            print("Tables ensured/created")
            return
        except OperationalError as e:
            print(f"DB not ready (attempt {attempt+1}/{retries}): {e}")
            time.sleep(2)
    raise RuntimeError("Cannot connect to DB to create tables after several retries.")

@app.post("/items/", response_model=schemas.Item)
def create_item_endpoint(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)

@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db, skip=skip, limit=limit)

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.put("/items/{item_id}", response_model=schemas.Item)
def update_item_endpoint(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    db_item = crud.update_item(db, item_id, item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.delete("/items/{item_id}", response_model=schemas.Item)
def delete_item_endpoint(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
