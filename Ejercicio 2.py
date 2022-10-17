# Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
# Si el divisor es cero el programa debe mostrar un error.
divisor = float(input("Introduzca un número como divisor:\n"))
dividendo = float(input("Introduzca un número como dividendo:\n"))

division = divisor/dividendo

while divisor == 0:
    divisor = input("Ha ocurrido un ERROR\n")

if divisor > 0:
    print("El resultado es: " + str(division))
