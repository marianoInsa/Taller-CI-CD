import pytest
from httpx import AsyncClient, ASGITransport
from fastapi import status
from app.main import app

@pytest.mark.asyncio
async def test_root_valido():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hola Mundo!"}

@pytest.mark.asyncio
async def test_root_invalido():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/invalido")
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_cantidad_letras_valido():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {"texto": "Hola mundo"}
        response = await ac.post("/cantidad_letras", json=payload)
    assert response.status_code == 200
    assert response.json()["cantidad"] == len("Holamundo")

@pytest.mark.asyncio
async def test_cantidad_letras_invalido():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {"text": "Hola mundo"}
        response = await ac.post("/cantidad_letras", json=payload)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_cantidad_palabras_valido():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {"texto": "Hola mundo", "cant": 5}
        response = await ac.post("/cantidad_palabras", json=payload)
    assert response.status_code == 200
    assert response.json()["cantidad"] == 1

@pytest.mark.asyncio
async def test_cantidad_palabras_invalido():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {"text": "hola", "cant": 4}
        response = await ac.post("/cantidad_palabras", json=payload)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_cantidad_palabras_invalido():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {"texto": "hola", "cantidad": 4}
        response = await ac.post("/cantidad_palabras", json=payload)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_cantidad_palabras_invalido():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {"texto": "hola"}
        response = await ac.post("/cantidad_palabras", json=payload)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_cantidad_palabras_invalido():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {"cant": 2}
        response = await ac.post("/cantidad_palabras", json=payload)
    assert response.status_code == 422