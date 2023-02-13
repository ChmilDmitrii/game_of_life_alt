import uuid
from sqlalchemy import Boolean, Column, Integer, UUID, JSON

from .database import Base


class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True, index=True)
    unique = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4)
    lines = Column(Integer)
    columns = Column(Integer)
    alive_cells = Column(JSON)
    game_over = Column(Boolean, default=False)
