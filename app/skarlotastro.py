import os

def abrir_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print("El archivo no existe.")
        return ""

def guardar_archivo(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(contenido)
        print("Archivo guardado correctamente.")
    except:
        print("Error al guardar el archivo.")

def menu():
    print("1. Abrir archivo")
    print("2. Guardar archivo")
    print("3. Salir")

def editor_textos():
    while True:
        menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre_archivo = input("Ingrese el nombre del archivo a abrir: ")
            contenido = abrir_archivo(nombre_archivo)
            print("Contenido del archivo:\n", contenido)

        elif opcion == "2":
            nombre_archivo = input("Ingrese el nombre del archivo a guardar: ")
            contenido = input("Ingrese el contenido del archivo: ")
            guardar_archivo(nombre_archivo, contenido)

        elif opcion == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    editor_textos()
