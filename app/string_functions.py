import re

def contar_caracteres(texto: str) -> int:
    """Cuenta la cantidad de caracteres (letras o números) en el texto sin contar caracteres especiales."""
    suma = 0

    if not texto.strip():
        raise ValueError("Debe ingresar un texto como entrada.")
    suma = len(re.findall(r'[a-zA-Z0-9]', texto))
    if suma == 0:
        raise ValueError("El texto no contiene letras o números.")

    return suma

def contar_palabras(texto: str, cant: int) -> int:
    """Cuenta la cantidad de palabras de `cant` caracteres en el texto."""
    if cant <= 0:
        raise ValueError("La cantidad de caracteres debe ser mayor a 0.")
    
    if not texto.strip() or texto.isdigit():
        raise ValueError("Debe ingresar un texto como entrada.")
    
    palabras = texto.split()

    suma = 0
    flag = False
    for palabra in palabras:
        if re.search(r'[a-zA-Z]', palabra):
            flag = True
            solo_letras = re.sub(r'[^a-zA-Z]', '', palabra)
            if len(solo_letras) == cant:
                suma += 1

    if not flag:
        raise ValueError("El texto no contiene palabras válidas.")

    return suma

if __name__ == "__main__":
    # texto = "Hola mundo! 1234"
    texto = "10 + 20 = 30"
    print(f"Cantidad de caracteres: {contar_caracteres(texto)}")
    cant = int(input("Ingrese la cantidad de caracteres de las palabras a contar: "))
    print(f"Cantidad de palabras de {cant} caracteres: {contar_palabras(texto, cant)}")