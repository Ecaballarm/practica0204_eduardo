# Escribir un programa que pida al usuario un número entero y
# muestre por pantalla un triángulo rectángulo como el de más abajo.

numero = int(input("Introduce el número: "))
for i in range(1, numero+1, 2):
    for k in range(i, 0, -2):
        print(k, end=" ")
    print("")