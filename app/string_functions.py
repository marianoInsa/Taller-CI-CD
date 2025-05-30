def contar_caracteres(texto: str) -> int:
    """Cuenta la cantidad de caracteres (letras o números) en el texto sin contar caracteres especiales."""
    suma = 0
    for caracter in texto:
        if caracter.isalnum():
            suma += 1
    return suma

def contar_palabras(texto: str, cant: int) -> int:
    """Cuenta la cantidad de palabras de `cant` caracteres en el texto."""
    if cant <= 0:
        raise ValueError("La cantidad de caracteres debe ser mayor a 0.")
    
    palabras = texto.split()

    suma = 0
    for palabra in palabras:
        if any(c.isdigit() for c in palabra):
            continue

        solo_letras = ''.join(c for c in palabra if c.isalpha())

        if len(solo_letras) == cant:
            suma += 1
    return suma

if __name__ == "__main__":
    # texto = "Hola mundo! 1234"
    texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi maximus leo dapibus, tincidunt felis pulvinar, accumsan tortor. Aliquam eros turpis, dapibus ut ante dictum, egestas auctor tortor. Suspendisse eu ante eget nibh suscipit auctor at in tortor. Quisque ut feugiat metus. Proin finibus cursus tincidunt. Nunc nulla leo, feugiat non."
    print(f"Cantidad de caracteres: {contar_caracteres(texto)}")
    cant = int(input("Ingrese la cantidad de caracteres de las palabras a contar: "))
    print(f"Cantidad de palabras de {cant} caracteres: {contar_palabras(texto, cant)}")