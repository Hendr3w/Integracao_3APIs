from sqlalchemy import Column, Integer, String
from api_spotify.database import Base

class Track(Base):
    __tablename__="tracks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    artist = Column(String)
    album = Column(String)
    genre = Column(String)
    duration = Column(Integer) # Em segundos
    year = Column(Integer)
