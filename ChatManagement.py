from UsrManagement import *
import json
import re

carpeta_usr = "usr" #carpeta para guardar los usuarios
carpeta_conv = "conv" #carpeta para guardar las conversaciones


def escribirArchivosConv(nombreUsr, conversacion):
    """Método que escribe las conversaciones en los archivos que estan en la carpeta de conversaciones

    Args:
        nombreUsr (str): _description_
        conversacion (_type_): _description_
    """
    carpeta = "conv"
    rutaArchivo = os.path.join(carpeta, f"{nombreUsr}Historial.json") # La ruta de la conversación estará en un json


    # Crear la carpeta si no existe
    if os.path.exists(rutaArchivo):
        try:
            with open(rutaArchivo, "r", encoding="utf-8") as archivo:
                historialConv = json.load(archivo)
        except json.JSONDecodeError:
            print("Error al leer el historial. Se sobrescribirá el archivo.")
            historialConv = []
    else:
        historialConv = []  # Si no existe, se crea una lista vacía#si no existe crea una lista vacía para almacenar el historial de conversacion



    # Convertir el historial en una lista de diccionarios con formato {"usuario": ..., "chatgpt": ...}
    nueva_conversacion = []
    for usuario, chatgpt in zip(conversacion[1::2], conversacion[2::2]):  # Salta el primer mensaje del sistema
        nueva_conversacion.append([usuario["content"], chatgpt["content"]])

    if nueva_conversacion:
        historialConv.append(nueva_conversacion)  # Agrega la nueva conversación

    # Guardar en formato JSON con indentación para mejor legibilidad
    with open(rutaArchivo, "w", encoding="utf-8") as archivo:
        json.dump(historialConv, archivo, ensure_ascii=False, indent=4)



#--------Codigo sin Usar
def cargarArchivosConv(nombreUsr):
    """Método que carga los archivos que estan en la carpeta de conversaciones

    Args:
        nombreUsr (str): Nombre de usuario del inicio de sesión

    Returns:
        list: retorna la lectura de todas las líneas del archivo
    """
    carpeta = "conv"
    rutaArchivo = os.path.join(carpeta, f"{nombreUsr}Historial.json")

    if not os.path.exists(rutaArchivo):
        print("No hay historial previo. Empezando una nueva conversación.")
        return [{"role": "system", "content": "Eres un asistente útil y conversacional."}]

    with open(rutaArchivo, "r", encoding="utf-8") as archivo:
        try:
            historial = json.load(archivo)
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON. Se iniciará una conversación nueva.")
            return [{"role": "system", "content": "Eres un asistente útil y conversacional."}]

    conversacion = [{"role": "system", "content": "Eres un asistente útil y conversacional."}]

    for bloque in historial:
        if isinstance(bloque, list) and len(bloque) >= 2:  # Asegura que haya datos válidos
            for i in range(1, len(bloque)):
                if isinstance(bloque[i], list) and len(bloque[i]) == 2:
                    conversacion.append({"role": "user", "content": bloque[i][0]})
                    conversacion.append({"role": "assistant", "content": bloque[i][1]})
    return conversacion


def historialConversaciones(nombreUsr):
    """Método para mostrar el historial de conversaciones

    Args:
        nombreUsr (_type_): _description_
    """
    carpeta = "conv"
    rutaArchivo = os.path.join(carpeta, f"{nombreUsr}Historial.json")

    if not os.path.exists(rutaArchivo):
        print("No hay historial de conversación disponible.")
        return

    try:
        with open(rutaArchivo, "r", encoding="utf-8") as archivo:
            historialCargado = json.load(archivo)
    except json.JSONDecodeError:
        print("Error al leer el historial. El archivo podría estar corrupto.")
        return

    print("\n--- HISTORIAL DE CONVERSACIÓN ---")
    for indice, intercambio in enumerate(historialCargado, start=1):
        print(f"\n--- Conversación {indice}: ---")
        for mensaje in intercambio:
            if isinstance(mensaje, list) and len(mensaje) == 2:  # Verifica formato esperado
                print(f"\nUsuario: {mensaje[0]}")
                print(f"ChatGPT: {mensaje[1]}")
            else:
                print("\n[Entrada inválida en el historial]")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n--- FIN DEL HISTORIAL ---")


def palabrasClave(nombreUsr):
    """Método para buscar una palabra clave en el historial de conversaciones.

    Args:
        nombreUsr (str): Nombre de usuario del historial.

    Returns:
        None: Imprime los resultados de la búsqueda.
    """
    carpeta = "conv"
    rutaArchivo = os.path.join(carpeta, f"{nombreUsr}Historial.json")


    try:
        with open(rutaArchivo, "r", encoding="utf-8") as archivo:
            historialCargado = json.load(archivo)
    except json.JSONDecodeError:
        print("Error al leer el historial. El archivo podría estar corrupto.")
        return

    palabraClave = input("Ingrese la palabra clave a buscar: ").strip() # Solicita la palabra clave
    if not palabraClave:
        print("No ingresaste ninguna palabra clave.")
        return
    

    # Códigos ANSI para color (amarillo en este caso)
    COLOR = "\033[31m"
    RESET = "\033[0m"


     # Expresión regular para buscar solo la palabra exacta (ignorando mayúsculas/minúsculas)
    regex = re.compile(rf"\b{re.escape(palabraClave)}\b", re.IGNORECASE)

    coincidencias = []

    print("\n--- RESULTADOS DE LA BÚSQUEDA ---")
    for indice, intercambio in enumerate(historialCargado, start=1):
        for mensaje in intercambio:
            if isinstance(mensaje, list) and len(mensaje) == 2:  # Verifica formato esperado
                usuario, chatgpt = mensaje
                if regex.search(usuario) or regex.search(chatgpt):  # Busca la palabra exacta
                    # Reemplaza la palabra exacta con color
                    palabra_usuario_resaltado = regex.sub(f"{COLOR}\\g<0>{RESET}", usuario)
                    palabra_chatgpt_resaltado = regex.sub(f"{COLOR}\\g<0>{RESET}", chatgpt)
                    coincidencias.append((indice, palabra_usuario_resaltado, palabra_chatgpt_resaltado))


    if coincidencias:
        for conv, usuario, chatgpt in coincidencias:
            print(f"\n--- Conversación {conv}: ---")
            print(f"Usuario: {usuario}")
            print(f"ChatGPT: {chatgpt}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("No se encontraron coincidencias con la palabra clave.")

    print("\n--- FIN DE LA BÚSQUEDA ---")



def resumirConversacion():
    """Método para resumir conversacion 
    """
    # carpeta = "conv"
    # rutaArchivo = os.path.join(carpeta, f"{nombreUsr}Historial.json")


    # try:
    #     with open(rutaArchivo, "r", encoding="utf-8") as archivo:
    #         historialCargado = json.load(archivo)
    # except json.JSONDecodeError:
    #     print("Error al leer el historial. El archivo podría estar corrupto.")
    #     return
    
    pass
    

