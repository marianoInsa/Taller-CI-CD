import pytest
from app.string_functions import contar_caracteres

def test_palabras_completas():
  assert contar_caracteres("Hola Mundo") == 9

def test_palabras_con_espacios():
  assert contar_caracteres("H o l a   M u n d o") == 9

def test_vacio():
  with pytest.raises(ValueError):
    contar_caracteres("")

def test_solo_espacios():
  with pytest.raises(ValueError):
    contar_caracteres("     ")

def test_caracteres_especiales():
  assert contar_caracteres("¡¡¡Hola, Mundo!!!") == 9

def test_solo_caracteres_especiales():
  with pytest.raises(ValueError):
    contar_caracteres("?¿!==")

def test_texto_largo():
  assert contar_caracteres("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi maximus leo dapibus, tincidunt felis pulvinar, accumsan tortor. Aliquam eros turpis, dapibus ut ante dictum, egestas auctor tortor. Suspendisse eu ante eget nibh suscipit auctor at in tortor. Quisque ut feugiat metus. Proin finibus cursus tincidunt. Nunc nulla leo, feugiat non.") == 279

def test_numeros():
  assert contar_caracteres("1234567890") == 10

def test_operaciones_matematicas():
  assert contar_caracteres("10 + 20 = 30") == 6

def test_caracteres_y_numeros():
  assert contar_caracteres("H 1 o 2 l 3 a 4") == 8