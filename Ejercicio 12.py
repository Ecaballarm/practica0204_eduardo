# Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input("Escribe una frase: ")
letra = input("Escribe una letra: ")
contador = 0

for i in frase:
    if i == letra:
        contador += 1
print("La " + letra + " aparece  veces en la frase")
