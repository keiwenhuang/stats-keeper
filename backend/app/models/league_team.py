from app.db.session import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class LeagueTeam(Base):
    __tablename__ = "league_teams"

    league_id = Column(Integer, ForeignKey("leagues.league_id"), primary_key=True)
    team_id = Column(Integer, ForeignKey("teams.team_id"), primary_key=True)

    # Relationships
    league = relationship("League")
    team = relationship("Team", back_populates="leagues")
