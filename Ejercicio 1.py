# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña e imprima
# por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable
# sin tener en cuenta mayúsculas y minúsculas.

password = "contraseña"

user_password = input("Introduce contraseña:\n")

while user_password.lower() != password:
    user_password = input("La contraseña es ERRONEA, introduce de nuevo la contraseña:\n")
if user_password.lower() == password.lower():
    print("La contraseña es CORRECTA")
else:
    print("La contraseña es ERRONEA")
