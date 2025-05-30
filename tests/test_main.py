from fastapi.testclient import TestClient
from app.main import app

app = TestClient(app)

def test_root():
    response = app.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hola Mundo!"}

def test_cantidad_letras():
    response = app.post("/cantidad_letras", json={"texto": "Hola Mundo"})
    assert response.status_code == 200
    assert response.json() == {"cantidad": 9}

def test_cantidad_palabras():
    response = app.post("/cantidad_palabras", json={"texto": "Hola Mundo", "cant": 4})
    assert response.status_code == 200
    assert response.json() == {"cantidad": 1}
    