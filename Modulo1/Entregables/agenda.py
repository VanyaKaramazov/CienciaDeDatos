# Agenda de contactos
import pandas as pd

def crear_agenda():
    # Usamos un diccionario para almacenar los contactos, donde la clave es el nombre y el valor es una lista de números de teléfono
    return {}

def agregar_contacto(agenda, nombre, numero):
    if nombre in agenda:
        agenda[nombre].append(numero)   # agrega sin borrar los anteriores
    else:
        agenda[nombre] = [numero]       # crea un nuevo registro

def buscar_contacto(agenda, nombre):
    if nombre in agenda:
        return agenda[nombre]
    else:
        print("Contacto no encontrado en la agenda")
        return None

def eliminar_contacto(agenda, nombre):
    if nombre in agenda:
        del agenda[nombre]
    else:
        print("Contacto no encontrado en la agenda")


# Crear agenda vacía
agenda = crear_agenda()

# Agregar contactos
agregar_contacto(agenda, "Pedro", "5551234")
agregar_contacto(agenda, "Pedro", "5555678")  # agregamos otro numero al mismo contacto
agregar_contacto(agenda, "Ana", "5559999")

# Buscar contactos
print(buscar_contacto(agenda, "Pedro"))  
print(buscar_contacto(agenda, "Luis"))   # imprime mensaje de no encontrado

# Eliminar contacto
eliminar_contacto(agenda, "Ana")
print(buscar_contacto(agenda, "Ana"))    # imprime mensaje de no encontrado


# Convertir la agenda a un DataFrame
df_agenda = pd.DataFrame([
    {"nombre": nombre, "telefono": numero}
    for nombre, numeros in agenda.items()
    for numero in numeros
])
print(df_agenda)
