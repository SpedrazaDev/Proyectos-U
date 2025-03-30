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
        with open(rutaArchivo, "r",encoding="utf-8") as archivo:
            return json.load(archivo)
    else:
        return None

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




         
    

