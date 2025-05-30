from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

class TextoModel(BaseModel):
    texto: str

def contar_caracteres(texto: str) -> int:
    """Cuenta la cantidad de caracteres en el texto sin contar espacios en blanco."""
    return len(texto.replace(" ", ""))

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