# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N
# y el grupo B por el resto.
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("Escribe tu nombre: ")
sexo = input("Escribe tu sexo (H o M): ")

if sexo =="M":
    if nombre[0].lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if nombre[0].lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)