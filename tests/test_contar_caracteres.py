import pytest
from app.string_functions import contar_caracteres

def test_contar_caracteres():
    assert contar_caracteres("Hola Mundo") == 9
    assert contar_caracteres("H o l a   M u n d o") == 9
    assert contar_caracteres("") == 0
    assert contar_caracteres("     ") == 0
    assert contar_caracteres("¡¡¡Hola, Mundo!!!") == 9
    assert contar_caracteres("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi maximus leo dapibus, tincidunt felis pulvinar, accumsan tortor. Aliquam eros turpis, dapibus ut ante dictum, egestas auctor tortor. Suspendisse eu ante eget nibh suscipit auctor at in tortor. Quisque ut feugiat metus. Proin finibus cursus tincidunt. Nunc nulla leo, feugiat non.") == 279
    assert contar_caracteres("1234567890") == 10
    assert contar_caracteres("10 + 20 = 30") == 6
    assert contar_caracteres("H 1 o 2 l 3 a 4") == 8