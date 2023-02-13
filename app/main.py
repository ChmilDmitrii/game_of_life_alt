from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/game/", response_model=schemas.GameCreate)
def create_game(db: Session = Depends(get_db)):
    return crud.create_game(db=db)


@app.post("/game/{unique}", response_model=schemas.GameUpdated)
def next_step(unique: str, db: Session = Depends(get_db)):
    db_game = crud.get_game(db=db, unique=unique)
    if not db_game:
        raise HTTPException(status_code=400,
                            detail="The game has not been created")
    return crud.update_game(db=db, db_game=db_game)
