from database import SessionLocal, engine
from api_spotify.models import Track, Base

Base.metadata.create_all(bind=engine)

session = SessionLocal()

musicas = [
    Track(name="Bohemian Rhapsody", artist="Queen", album="A Night at the Opera", genre="Rock", duration=354, year=1975),
    Track(name="Imagine", artist="John Lennon", album="Imagine", genre="Soft Rock", duration=183, year=1971),
    Track(name="Hotel California", artist="Eagles", album="Hotel California", genre="Rock", duration=391, year=1976),
    Track(name="Billie Jean", artist="Michael Jackson", album="Thriller", genre="Pop", duration=294, year=1982),
    Track(name="Smells Like Teen Spirit", artist="Nirvana", album="Nevermind", genre="Grunge", duration=301, year=1991),
    Track(name="Hey Jude", artist="The Beatles", album="Hey Jude", genre="Rock", duration=431, year=1968),
    Track(name="Like a Rolling Stone", artist="Bob Dylan", album="Highway 61 Revisited", genre="Folk Rock", duration=369, year=1965),
    Track(name="Shake It Off", artist="Taylor Swift", album="1989", genre="Pop", duration=242, year=2014),
    Track(name="Lose Yourself", artist="Eminem", album="8 Mile", genre="Hip-Hop", duration=326, year=2002),
    Track(name="Rolling in the Deep", artist="Adele", album="21", genre="Pop Soul", duration=228, year=2010),
    Track(name="Uptown Funk", artist="Mark Ronson ft. Bruno Mars", album="Uptown Special", genre="Funk Pop", duration=269, year=2014),
    Track(name="Take On Me", artist="A-ha", album="Hunting High and Low", genre="Synthpop", duration=225, year=1985),
    Track(name="Wonderwall", artist="Oasis", album="(What's the Story) Morning Glory?", genre="Britpop", duration=259, year=1995),
    Track(name="HUMBLE.", artist="Kendrick Lamar", album="DAMN.", genre="Hip-Hop", duration=177, year=2017),
    Track(name="Bad Guy", artist="Billie Eilish", album="When We All Fall Asleep, Where Do We Go?", genre="Pop", duration=194, year=2019),
]

session.add_all(musicas)
session.commit()
session.close()

print("Banco populado com 15 músicas detalhadas!")