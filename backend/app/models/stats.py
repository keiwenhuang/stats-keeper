from app.db.session import Base
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship


class PlayerStats(Base):
    __tablename__ = "player_stats"

    stat_id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.game_id"), nullable=False)
    player_id = Column(Integer, ForeignKey("players.player_id"), nullable=False)
    pts = Column(Integer, default=0)
    rebs = Column(Integer, default=0)
    asts = Column(Integer, default=0)
    stls = Column(Integer, default=0)
    blks = Column(Integer, default=0)
    turnovers = Column(Integer, default=0)
    fouls = Column(Integer, default=0)
    fg2m = Column(Integer, default=0)
    fg2a = Column(Integer, default=0)
    fg3m = Column(Integer, default=0)
    fg3a = Column(Integer, default=0)
    fgm = Column(Integer, default=0)
    fga = Column(Integer, default=0)
    ftm = Column(Integer, default=0)
    fta = Column(Integer, default=0)
    dnp = Column(Boolean, default=False)
    fp = Column(Float(5, 2), default=0.0)

    # Relationships
    game = relationship("Game", back_populates="player_stats")
    player = relationship("Player", back_populates="stats")
