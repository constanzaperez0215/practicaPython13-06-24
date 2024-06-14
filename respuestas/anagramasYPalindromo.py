print('---------------------Anagramas--------------------------------')
palabra1= str(input('Ingrese la primera palabra: '))
palabra2= str(input('Ingrese la segunda palabra: '))

def anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    return sorted(palabra1) == sorted(palabra2)
    #sorted ordena las letas de la variable en orden alfabetico, por eso lo compara y si son iguales son anagramas.

if anagrama(palabra1,palabra2):
    print(f'{palabra1} y {palabra2} son anagramas.')
else:
    print(f'{palabra1} y {palabra2} NO son anagramas.')


print('---------------------Palíndromos--------------------------------')

def es_palindromo(frase):
    # Convertir a minúsculas y eliminar espacios y puntuación
    frase_limpia = ''.join(caracter for caracter in frase if caracter.isalnum()).lower()
    # ''.join() toma cada carácter generado y los une en una sola cadena sin ningún separador
    # Comparar la frase limpia con su versión invertida
    return frase_limpia == frase_limpia[::-1]

# Ejemplo de uso
frase = str(input('Ingrese una frases: '))
# palindromo  "Anita lava la tina"

if es_palindromo(frase):
    print(f'"{frase}" es un palindromo')  # Salida: True
else:
    print(f'"{frase}" NO es un palindromo')