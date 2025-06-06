import pytest
from app.string_functions import contar_palabras

def test_palabras_y_cantidad_completas():
  assert contar_palabras("Hola Mundo", 4) == 1

def test_palabras_con_espacios():
  assert contar_palabras("H o l a   M u n d o", 4) == 0

def test_palabra_con_caracteres_especiales():
  assert contar_palabras("¡¡¡Hola, Mundo!!!", 4) == 1

def test_palabras_con_caracteres_especiales_en_medio():
  assert contar_palabras("H 1 o 2 l 3 a 4 aa", 1) == 4

def test_palabra_vacia():
  with pytest.raises(ValueError):
    contar_palabras("", 4)

def test_palabra_solo_con_espacios():
  with pytest.raises(ValueError):
    contar_palabras("    ", 4)

def test_cantidad_vacia():
  with pytest.raises(ValueError):
    contar_palabras("Hola", 0)

def test_cantidad_negativa():
  with pytest.raises(ValueError):
      contar_palabras("Texto", -1)

def test_texto_largo():
  assert contar_palabras("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi maximus leo dapibus, tincidunt felis pulvinar, accumsan tortor. Aliquam eros turpis, dapibus ut ante dictum, egestas auctor tortor. Suspendisse eu ante eget nibh suscipit auctor at in tortor. Quisque ut feugiat metus. Proin finibus cursus tincidunt. Nunc nulla leo, feugiat non.", 5) == 8

def test_solo_numeros():
  with pytest.raises(ValueError):
      contar_palabras("1234567890", 10)

def test_sin_palabras():
  with pytest.raises(ValueError):
    contar_palabras("10 + 20 = 30", 2)