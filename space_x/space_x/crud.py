from sqlalchemy.orm import Session

from . import models, schemas


def get_rockets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Rocket).offset(skip).limit(limit).all()


def get_launches(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Rocket).offset(skip).limit(limit).all()
