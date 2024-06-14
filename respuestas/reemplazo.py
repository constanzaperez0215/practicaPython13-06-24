frase = 'Hola Mundo Les Dice Constanza'

def reemplazo_mayusculas(frase):
    nueva_frase = ''.join(['$' if letra.isupper() else letra for letra in frase])
    print(nueva_frase)