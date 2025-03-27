from API import chat_con_php
import UsrManagement 
import openai


def menu_main():
    
    print("-----Menu de Opciones-----")
    print("1. Iniciar Sesion")
    print("2. Registrar Usuario")
    print("3. Salir")

    
    choice = int(input("Seleccione la opcion que desea realizar: "))

    if choice == 1:
        UsrManagement.inicioSesion()
        return False
    elif choice == 2:
        UsrManagement.registroUsusuarios()
        return False
    elif choice == 3:
         exit()
    else:
            print("Digite una opcion valida.")
            return(menu_main)

    



def submenu():
    print("-----Menu de Inicio Sesion-----")
    print("1. Chat")
    print("2. Historial de Conversaciones")
    print("")



def chat():
    # Mensaje de bienvenida para el usuario.
    print("Bienvenido al chat con ChatGPT (vía PHP). Escribe 'salir' para terminar.")
    # Ciclo de conversación donde el usuario puede interactuar con el asistente hasta que escriba 'salir'.
    while True:
        mensaje = input("Tú: ")  # Se solicita un mensaje al usuario.
        
        # Si el usuario escribe 'salir', 'exit' o 'quit', finaliza el chat.
        if mensaje.lower() in ["salir", "exit", "quit"]:
            print("ChatGPT: ¡Hasta luego!")
            break  # Se rompe el bucle y termina el programa.

        # Se envía el mensaje del usuario al servidor PHP y se recibe la respuesta.
        respuesta = chat_con_php(mensaje)
        
        # Se muestra la respuesta en la terminal.
        print(f"ChatGPT: {respuesta}")

while True:
    menu_main()