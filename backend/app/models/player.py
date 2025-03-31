from app.db.session import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Player(Base):
    __tablename__ = "players"

    player_id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("teams.team_id"), nullable=False)
    name = Column(String(50), nullable=False)
    jersey_number = Column(Integer)

    # Relationships
    team = relationship("Team", back_populates="players")
    stats = relationship("PlayerStats", back_populates="player")
