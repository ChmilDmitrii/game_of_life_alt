import uuid
from sqlalchemy.orm import Session

from . import models, game


def get_game(db: Session, unique: str):
    return db.query(models.Game).filter(
        models.Game.unique == uuid.UUID(unique)).first()


def create_game(db: Session):
    db_game = models.Game(
        lines=50,
        columns=50,
        alive_cells=[],
    )
    game.GameOfLife.create_game(db_game)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def update_game(db: Session, db_game: models.Game):
    game.GameOfLife(db_game).next_step()
    db.commit()
    db.refresh(db_game)
    return db_game
