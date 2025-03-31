from app.db.session import Base
from sqlalchemy import (
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import relationship


class Game(Base):
    __tablename__ = "games"

    game_id = Column(Integer, primary_key=True, index=True)
    league_id = Column(Integer, ForeignKey("leagues.league_id"), nullable=False)
    home_team_id = Column(Integer, ForeignKey("teams.team_id"), nullable=False)
    away_team_id = Column(Integer, ForeignKey("teams.team_id"), nullable=False)
    youtube_url = Column(String(255))
    status = Column(String(20), default="scheduled", nullable=False)
    home_score = Column(Integer, default=0)
    away_score = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Constraints
    __table_args__ = (
        CheckConstraint(
            "status IN ('scheduled', 'in_progress', 'completed', 'cancelled')"
        ),
    )

    # Relationships
    league = relationship("League")
    home_team = relationship(
        "Team", foreign_keys=[home_team_id], back_populates="home_games"
    )
    away_team = relationship(
        "Team", foreign_keys=[away_team_id], back_populates="away_games"
    )
    player_stats = relationship("PlayerStats", back_populates="game")
