import os
list_nombres = []
list_apellidos = []
list_id = []
list_correo = []
list_contacto = []
list_edad = []
list_a_experiencia = []
list_profesion = []
list_ciudad = []
list_sexo = []


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def registrar_candidato():
    nombre = input("Ingrese nombres completos: ")
    apellidos = input("Ingrese apellidos completos: ")
    identificacion = input("Ingrese identificación: ")
    correo = input("Ingrese correo electrónico: ")
    contacto = input("Ingrese número de contacto/telefono: ")
    edad = int(input("Ingrese edad: "))
    experiencia = int(input("Ingrese años de experiencia: "))
    profesion = input("Ingrese profesión: (Ing. Sistemas o Ing. Informática): ").lower()
    ciudad = input("Ingrese ciudad: ")
    sexo = input("Ingrese sexo (F/M): ")

    if 25 <= edad <= 35 and profesion in ["ing. sistemas", "ing. informática"] and 2 <= experiencia <= 4:
        list_nombres.append(nombre)
        list_apellidos.append(apellidos)
        list_id.append(identificacion)
        list_correo.append(correo)
        list_contacto.append(contacto)
        list_edad.append(edad)
        list_a_experiencia.append(experiencia)
        list_profesion.append(profesion)
        list_ciudad.append(ciudad)
        list_sexo.append(sexo)
        
        print("Candidato registrado con éxito.")
    else:
        print("El candidato registrado no cumple con los requisitos.")


def consultar_candidatos():
    limpiar_pantalla()
    if list_nombres:
        print("Lista de candidatos:")
        for i in range(len(list_nombres)):
            print(f"Nombre: {list_nombres[i]}, Apellidos: {list_apellidos[i]}, ID: {list_id[i]}, Correo: {list_correo[i]}, Contacto: {list_contacto[i]}, Edad: {list_edad[i]}, Experiencia: {list_a_experiencia[i]}, Profesión: {list_profesion[i]}, Ciudad: {list_ciudad[i]}, Sexo: {list_sexo[i]}")
    else:
        print("Lo siento pero no hay candidatos registrados.")


while True:
    limpiar_pantalla()
    def fnt_limpiar():
        os.system('cls')
    print('Autor: Michell Mosquera')
    print('Fecha: 18 de abril del 2024\n\n')
    
    print(" ---- MENU ----")
    print("1. Registrar candidato")
    print("2. Consultar candidatos")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        limpiar_pantalla()
        registrar_candidato()
        input("Presione ENTER para volver al menú...")
    elif opcion == "2":
        consultar_candidatos()
        input("Presione ENTER para volver al menú...")
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Lo siento la oción no válida. Por favor, seleccione una opción válida.")
