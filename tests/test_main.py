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
