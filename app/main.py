from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from app.string_functions import contar_caracteres, contar_palabras

app = FastAPI()

class TextoModel(BaseModel):
    texto: str

class TextoCantidadModel(BaseModel):
    texto: str
    cant: int

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Hola Mundo!"}

@app.post("/cantidad_letras")
async def cantidad_letras(request: TextoModel):
    try:
        cantidad = contar_caracteres(request.texto)
        return {"cantidad": cantidad}
    except Exception as e:
        return {"error": str(e)}
    
@app.post("/cantidad_palabras")
async def cantidad_palabras(request: TextoCantidadModel):
    try:
        cantidad = contar_palabras(request.texto, request.cant)
        return {"cantidad": cantidad}
    except ValueError as e:
        return {"error": str(e)}