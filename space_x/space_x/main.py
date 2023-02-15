from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/rockets/", response_model=list[schemas.Rocket])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rockets = crud.get_rockets(db, skip=skip, limit=limit)
    return rockets
