import json
import os

carpeta_usr = "usr" #carpeta para guardar los usuarios
carpeta_conv = "conv" #carpeta para guardar las conversaciones


def cargarArchivosUsr(nombreUsr):
    """Método que carga los archivos que estan en la carpeta de usuarios

    Args:
        nombreUsr (str): Nombre de usuario del inicio de sesión

    Returns:
        dict: retorna el diccionario que esta en el archivo txt
    """
    rutaArchivo = os.path.join(carpeta_usr, f"{nombreUsr}_usr.txt")
    if os.path.exists(rutaArchivo):
        with open(rutaArchivo, "r") as archivo:
            return json.load(archivo)
    else:
        return None

def cargarArchivosConv(nombreUsr):
    """Método que carga los archivos que estan en la carpeta de conversaciones

    Args:
        nombreUsr (str): Nombre de usuario del inicio de sesión

    Returns:
        list: retorna la lectura de todas las líneas del archivo
    """
    rutaArchivo = os.path.join(carpeta_conv, f"{nombreUsr}_conv.txt")
    if os.path.exists(rutaArchivo):
        with open(rutaArchivo, "r") as archivo:
            return archivo.readlines()  # Lee las líneas directamente
    else:
        return []  # Retorna una lista vacía si no existe el archivo

def escribirArchivosConv(nombreUsr, mensaje, respuesta):
    """Método que escribe las conversaciones en los archivos que estan en la carpeta de conversaciones
    Args:
        nombreUsr (str): Nombre de usuario del inicio de sesión
        mensaje (str): Mensaje que se escribio en la conversación
        respuesta (str): Respuesta que dio chatgpt ante el mensaje
    """
    rutaArchivo = os.path.join(carpeta_conv, f"{nombreUsr}_conv.txt")
    
    conversaciones = cargarArchivosConv(nombreUsr) # Cargar el historial existente

    conversaciones.append(f"Tú: {mensaje}\nChatGPT: {respuesta}\n") # Agregar el nuevo mensaje y respuesta al historial
    
    with open(rutaArchivo, "w", encoding="utf-8") as archivo: # Escribir el historial completo en el archivo
        archivo.writelines(conversaciones)  # Escribimos todas las líneas de la lista



def inicioSesion():
    """Método para iniciar sesión en el programa

    Returns:
         nombreUsr (str): Nombre de usuario del inicio de sesión
    """
    nombreUsr= input("Ingrese su nombre de Inicio Sesión: ")
    Usrpsw= input("Ingrese su contraseña: ")

    usuario = cargarArchivosUsr(nombreUsr)
    if usuario and usuario["username"] == nombreUsr and usuario["password"] == Usrpsw:
         print(f"Acceso permitido. ¡Bienvenido {nombreUsr}!")
         return nombreUsr
    else:
        print("Acceso denegado. Usuario o contraseña incorrectos.")

def registroUsusuarios():
    """Método para registrar un nuevo usuario en el programa
    """
    nombreUsr= input("Ingrese su nombre: ")

    usuario = cargarArchivosUsr(nombreUsr)
    if usuario:
        print("El nombre de usuario ya está en uso. Intente con otro.")
        return
    
    Usrpsw= input("Ingrese su contraseña: ")
    usuario = {"username": nombreUsr, "password": Usrpsw}

    rutaArchivo = os.path.join(carpeta_usr, f"{nombreUsr}_usr.txt")
    with open(rutaArchivo, "w") as archivo:
        json.dump(usuario, archivo)

    print("Usuario agregado con éxito.")

    # print(f"Usuario '{nombreUsr}' registrado exitosamente.")
    # print(usuario)

def historialConversaciones(nombreUsr):
    """Método para mostrar el historial de conversaciones

    Args:
        nombreUsr (_type_): _description_
    """
    usuario = cargarArchivosUsr(nombreUsr)
    if usuario and usuario["username"] == nombreUsr:
         print(f"Acceso permitido. ¡Bienvenido al Historial de Conversaciones de {nombreUsr}!")
    else:
        print("Usuario no encontrado.")
        return  
    
    conversaciones = cargarArchivosConv(nombreUsr)

    if conversaciones:
        print("Historial de Conversaciones:")
        for i, conv in enumerate(conversaciones):  # Recorremos las conversaciones y las mostramos
            print(f"{i + 1}. {conv.strip()}")  # Mostrar sin los saltos de línea
    else:
        print("No hay conversaciones guardadas.")

         
    

