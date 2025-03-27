import os

Usuarios={
    
}



def inicioSesion():
    nombreUsr= input("Ingrese su nombre de Inicio Sesión: ")
    Usrpsw= input("Ingrese su contraseña: ")

    if nombreUsr in Usuarios and Usuarios[nombreUsr] == Usrpsw:
         print(f"Acceso permitido. ¡Bienvenido {nombreUsr}!")
    else:
        print("Acceso denegado. Usuario o contraseña incorrectos.")

def registroUsusuarios():
    nombreUsr= input("Ingrese su nombre: ")

    if nombreUsr in Usuarios:
        print("El nombre de usuario ya está en uso. Intente con otro.")
        return
    
    Usrpsw= input("Ingrese su contraseña: ")
    Usuarios[nombreUsr] = Usrpsw

    carpeta = "usr"
    ruta_archivo = os.path.join(carpeta, f"{nombreUsr}.txt")

   
    with open(ruta_archivo, "w") as archivo:
        archivo.write(f"{nombreUsr}:{Usrpsw}\n")

    print(f"Usuario '{nombreUsr}' registrado exitosamente.")
    print(Usuarios)

