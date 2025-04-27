import requests
import time
from flask import Flask, jsonify, request
from db import init_db, SessionLocal, User

API_URL = "http://localhost:5001"  
THIRD_API_URL = "http://localhost:5002"
logged_user = None 

init_db()

app = Flask(__name__)
#-----------------Funções de Login e dados de Usuário-----------------#
#Vamos usar um usuário padrão nessa versão. 
def register_default_user():
    db = SessionLocal()
    username = "hendrew"  
    password = "senha123" 

    user = db.query(User).filter(User.username == username).first()
    if not user:
        print(f"Registrando usuário padrão '{username}'...")
        db_user = User(username=username, password=password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    else:
        print(f"Usuário '{username}' já registrado.")
    db.close()

def login_user():
    global logged_user
    db = SessionLocal()
    username = "hendrew"
    user = db.query(User).filter(User.username == username).first()
    db.close()

    if user:
        logged_user = user
        print(f"Usuário '{username}' logado com sucesso.")
    else:
        print(f"Usuário '{username}' não encontrado!")



#-----------------Funções que se comunicam com as outras APIs-----------------#
def get_recommendations():
    try:
        response = requests.get(f"{API_URL}/recommendations")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def filter_favorites(tracks):
    favorites = [track for track in tracks if track['genre'] == 'Rock']
    return favorites

def send_favorites_to_third_api(favorites):
    try:
        response = requests.post(f"{THIRD_API_URL}/favorites", json={"favorites": favorites})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    
def pretty_print_favorites(favorites):
    if not favorites:
        print("Nenhum favorito encontrado para o gênero 'Rock'.")
    else:
        print("Favoritos encontrados (gênero 'Rock'):")
        for idx, track in enumerate(favorites, start=1):
            print(f"\n{idx}. Nome: {track['name']}")
            print(f"   Artista: {track['artist']}")
            print(f"   Álbum: {track['album']}")
            print(f"   Gênero: {track['genre']}")
            print(f"   Duração: {track['duration']} segundos")
            print(f"   Ano: {track['year']}")


#-----------------Rotas Flask para responder requisições das outras APIs e ou Usuários-----------------#
@app.route('/register', methods=['POST'])
def register_user():
    try:
       
        data = request.json
        username = data.get('username')
        password = data.get('password')

        db = SessionLocal()
        db_user = User(username=username, password=password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        db.close()

        return jsonify({"message": "Usuário registrado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_user/<username>', methods=['GET'])
def get_user(username):
    try:
        db = SessionLocal()
        user = db.query(User).filter(User.username == username).first()
        db.close()

        if user:
            return jsonify({"username": user.username, "password": user.password})
        else:
            return jsonify({"error": "Usuário não encontrado!"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
        print("Iniciando o processo de obtenção e filtragem de recomendações...\n")
        recommendations = get_recommendations()
        if "tracks" in recommendations:
            favorites = filter_favorites(recommendations["tracks"])
            #response = send_favorites_to_third_api(favorites)
            #print("Favoritos enviados para a terceira API:", response)
            pretty_print_favorites(favorites)
            app.run(host='0.0.0.0', port=5000)
        else:
            print("Erro ao obter recomendações:", recommendations)



        
