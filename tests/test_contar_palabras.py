import pytest
from app.string_functions import contar_palabras

def test_contar_palabras():
    assert contar_palabras("Hola Mundo", 4) == 1
    assert contar_palabras("H o l a   M u n d o", 4) == 0
    assert contar_palabras("", 4) == 0
    assert contar_palabras("     ", 4) == 0
    assert contar_palabras("¡¡¡Hola, Mundo!!!", 4) == 1
    assert contar_palabras("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi maximus leo dapibus, tincidunt felis pulvinar, accumsan tortor. Aliquam eros turpis, dapibus ut ante dictum, egestas auctor tortor. Suspendisse eu ante eget nibh suscipit auctor at in tortor. Quisque ut feugiat metus. Proin finibus cursus tincidunt. Nunc nulla leo, feugiat non.", 5) == 8
    assert contar_palabras("1234567890", 10) == 0
    assert contar_palabras("10 + 20 = 30", 2) == 0
    assert contar_palabras("H 1 o 2 l 3 a 4 aa", 1) == 4
    with pytest.raises(ValueError):
        contar_palabras("Texto de prueba", -1)
    with pytest.raises(ValueError):
        contar_palabras("Texto de prueba", 0)