from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/helloworld")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_funcao_teste():
    response = client.get("/funcaoteste")
    assert response.status_code == 200
    assert "num_aleatorio" in response.json()

def test_fatorial():
    response = client.get("/fatorial/5")
    assert response.status_code == 200
    assert response.json() == {"numero": 5, "fatorial": 120}

def test_num_aleatorios():
    response = client.get("/num_aleatorios/10/20")
    assert response.status_code == 200
    num = response.json()["numero_aleatorio"]
    assert 10 <= num <= 20

def test_converte_temperatura():
    response = client.get("/converte_temperatura/0")
    assert response.status_code == 200
    assert response.json() == {"celsius": 0, "fahrenheit": 32}