from app.db.session import Base
from sqlalchemy import Column, Integer, String


class League(Base):
    __tablename__ = "leagues"

    league_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    season = Column(String(5), nullable=False)
