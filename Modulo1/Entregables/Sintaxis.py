# mayor_edad.py
edad = int(input("Introduce tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# verificar_contraseña.py
contraseña_correcta = "micontraseña123"
contraseña_usuario = ""

while contraseña_usuario != contraseña_correcta:
    contraseña_usuario = input("Introduce la contraseña: ")
    if contraseña_usuario != contraseña_correcta:
        print("Contraseña incorrecta, intenta de nuevo.")

print("Contraseña correcta. Acceso concedido.")


# bienvenida_alumnos.py
alumnos = ["Ana", "Pedro", "Luis", "María"]

for alumno in alumnos:
    print(f"Bienvenido al curso, {alumno}.")
