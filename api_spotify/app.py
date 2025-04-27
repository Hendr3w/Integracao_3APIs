from flask import Flask, jsonify
from flask_caching import Cache
from api_spotify.database import SessionLocal
from api_spotify.models import Track

app = Flask(__name__)

app.config['CACHE_TYPE'] = 'RedisCache'
app.config['CACHE_REDIS_HOST'] = 'localhost'
app.config['CACHE_REDIS_PORT'] = 6379
app.config['CACHE_REDIS_DB'] = 0
app.config['CACHE_DEFAULT_TIMEOUT'] = 30

cache = Cache(app)


@app.route('/recommendations', methods=['GET'])
@cache.cached()
def recommendations():
    print("Requisição para /recommendations recebida!")
    session = SessionLocal()
    tracks = session.query(Track).all()
    session.close()
    return jsonify({
        "tracks": [
            {
                "name": t.name,
                "artist": t.artist,
                "album": t.album,
                "genre": t.genre,
                "duration": t.duration,
                "year": t.year
            }
            for t in tracks
        ]
    })


if __name__ == '__main__' or __name__ == 'api_spotify.app':
    print("Iniciando API Spotify...")  
    app.run(host='0.0.0.0', port=5001)