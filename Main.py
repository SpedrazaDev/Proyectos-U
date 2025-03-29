from API import chat_con_php
import UsrManagement
import openai


def menuMain():
    """Menú Principal, donde se inicia sesión, registra usuarios nuevos
    """
    while True:
        print("-----Menu de Opciones-----")
        print("1. Iniciar Sesion")
        print("2. Registrar Usuario")
        print("3. Salir")

        try:
            choice = int(input("Seleccione la opcion que desea realizar: "))
            if choice == 1:
                nomUsuario = UsrManagement.inicioSesion()  # Aquí recibimos el nombreUsr de inicioSesion
                if nomUsuario:  # Verificamos si el inicio de sesión fue exitoso (no es None)
                    subMenuInicioSesion(nomUsuario)  # Pasamos el nombreUsr al submenú
                else:
                    print("Error al iniciar sesión.")
            elif choice == 2:
                UsrManagement.registroUsusuarios()
                break  # Regresar al menú principal después de registrar
            elif choice == 3:
                print("¡Hasta luego!")
                exit()  # Salir del programa
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")



def subMenuInicioSesion(nombreUsr):
    """El submenú de la funcion de inicio de sesión

    Args:
        nombreUsr (str): el nombre de usuario con el que se inicio sesión
    """
    while True:
        print("-----Menu de Inicio Sesion-----")
        print("1. Chat")
        print("2. Historial de Conversaciones")
        print("3. Salir")

        try:
            choice = int(input("Seleccione la opcion que desea realizar: "))
            if choice == 1:
                chat(nombreUsr)
                break  # Regresar al submenú de inicio de sesión después del chat
            elif choice == 2:
                UsrManagement.historialConversaciones(nombreUsr)
                break  # Regresar al submenú de inicio de sesión
            elif choice == 3:
                return(menuMain())
            else:

                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


def chat(nombreUsr):
    """El chat con el que se conecta a chatgpt

    Args:
        nombreUsr (str): el nombre de usuario con el que se inicio sesión
    """
    print("Bienvenido al chat con ChatGPT (vía PHP). Escribe 'salir' para terminar.")
    while True:
        mensaje = input("Tú: ")  # Solicita el mensaje del usuario
        if mensaje.lower() in ["salir", "exit", "quit"]:
            print("ChatGPT: ¡Hasta luego!")
            break  # Termina el chat cuando el usuario escribe 'salir'
        respuesta = chat_con_php(mensaje)  # Llama a la función de PHP
        print(f"ChatGPT: {respuesta}")  # Muestra la respuesta del chat
        UsrManagement.escribirArchivosConv(nombreUsr, mensaje, respuesta)



menuMain()
