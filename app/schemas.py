import uuid
from typing import List
from pydantic import BaseModel


class GameBase(BaseModel):
    unique: uuid.UUID


class GameCreate(GameBase):
    pass

    class Config:
        orm_mode = True


class GameUpdated(GameBase):
    lines: int
    columns: int
    alive_cells: List[List[int]]
    game_over: bool

    class Config:
        orm_mode = True
