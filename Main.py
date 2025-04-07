import API
import UsrManagement
import ChatManagement
import shutil 


def menuMain():
    """Menú Principal, donde se inicia sesión, registra usuarios nuevos
    """
    while True:
        print("-----Menu Principal-----")
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
            elif choice == 2:
                menuHistorialConversaciones(nombreUsr)
            elif choice == 3:
                return(menuMain())
            else:

                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


def menuHistorialConversaciones(nombreUsr):
    """El submenú de la funcion de inicio de sesión

    Args:
        nombreUsr (str): el nombre de usuario con el que se inicio sesión
    """
    while True:
        print("-----Menú de Historial de Conversaciones-----")
        print("1. Historial")
        print("2. Buscar por palabra clave")
        print("3. Resumir Conversacion")
        print("4. Salir")

        try:
            choice = int(input("Seleccione la opcion que desea realizar: "))
            if choice == 1: 
                ChatManagement.historialConversaciones(nombreUsr)
            elif choice == 2:
                ChatManagement.palabrasClave(nombreUsr)
            elif choice == 3:
                ChatManagement.resumirConversacion(nombreUsr)
            elif choice == 4:
                return(subMenuInicioSesion(nombreUsr))
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
            ChatManagement.escribirArchivosConv(nombreUsr, API.conversacion)
            API.conversacion=[{"role": "system", "content": "Eres un asistente útil y conversacional."}]
            break  # Termina el chat cuando el usuario escribe 'salir'

            
        respuesta = API.chat_con_php(mensaje)  # Llama a la función de PHP
        print(f"ChatGPT: {respuesta}")  # Muestra la respuesta del chat

menuMain()
