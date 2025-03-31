from app.db.session import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Team(Base):
    __tablename__ = "teams"

    team_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)

    # Relationships
    players = relationship("Player", back_populates="team")
    home_games = relationship(
        "Game", foreign_keys="Game.home_team_id", back_populates="home_team"
    )
    away_games = relationship(
        "Game", foreign_keys="Game.away_team_id", back_populates="away_team"
    )
    leagues = relationship("LeagueTeam", back_populates="team")
