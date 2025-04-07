import requests
from API import URL_PHP
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
    for indice, intercambio in enumerate(historialCargado, start=1):    # Recorrer el historial de conversaciones cargado (historialCargado es una lista de bloques de conversación) enumerandolos desde el 1
        print(f"\n--- Conversación {indice}: ---")
        for mensaje in intercambio:
            if isinstance(mensaje, list) and len(mensaje) == 2:  # Verificar que el mensaje sea una lista con 2 elementos (usuario y ChatGPT)
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
    if not palabraClave:  # Verifica si el usuario no ingresó ninguna palabra clave
        print("No ingresaste ninguna palabra clave.")
        return
    

   
    COLOR = "\033[31m"  # Definir el color de resaltado en rojo
    RESET = "\033[0m"   # Definit el color original



    regex = re.compile(rf"\b{re.escape(palabraClave)}\b", re.IGNORECASE)  # Expresión regular para buscar solo la palabra exacta (ignorando mayúsculas/minúsculas)

    coincidencias = []   # Lista vacía que guardará las coincidencias encontradas

    print("\n--- RESULTADOS DE LA BÚSQUEDA ---")
    for indice, intercambio in enumerate(historialCargado, start=1):   # Recorrer el historial de conversaciones cargado (historialCargado es una lista de bloques de conversación)
        for mensaje in intercambio:    # Dentro de cada intercambio hay una lista de mensajes entre el usuario y el asistente
            if isinstance(mensaje, list) and len(mensaje) == 2:  # Verificar que el mensaje sea una lista con 2 elementos (usuario y ChatGPT)
                usuario, chatgpt = mensaje
                if regex.search(usuario) or regex.search(chatgpt):   # Si la palabra clave está presente en el mensaje del usuario o en el mensaje del asistente, se registra la coincidencia
                    # Reemplaza la palabra exacta con color
                    palabra_usuario_resaltado = regex.sub(f"{COLOR}\\g<0>{RESET}", usuario)
                    palabra_chatgpt_resaltado = regex.sub(f"{COLOR}\\g<0>{RESET}", chatgpt)
                    coincidencias.append((indice, palabra_usuario_resaltado, palabra_chatgpt_resaltado))  # Añade la conversación y los mensajes resaltados a la lista de coincidencias


    if coincidencias:   #Si se encuentran coincidencias, que se impriman al partir del siguiente formato
        for conv, usuario, chatgpt in coincidencias:
            print(f"\n--- Conversación {conv}: ---")
            print(f"Usuario: {usuario}")
            print(f"ChatGPT: {chatgpt}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("No se encontraron coincidencias con la palabra clave.")

    print("\n--- FIN DE LA BÚSQUEDA ---")



def resumirConversacion(nombreUsr):
    """Resume el historial de conversación guardado para un usuario en un máximo de 50 palabras 

    Args:
        nombreUsr (str): nombre del usuario que inicio sesión

    Returns:
        _type_: el resumen hecho
    """
    carpeta = "conv"
    rutaArchivo = os.path.join(carpeta, f"{nombreUsr}Historial.json")


    try:
        with open(rutaArchivo, "r", encoding="utf-8") as archivo:
            historialCargado = json.load(archivo)
    except json.JSONDecodeError:
        print("Error al leer el historial. El archivo podría estar corrupto.")
        return
    
    # Mostrar lista de conversaciones
    for i, conv in enumerate(historialCargado):  #Enumerar los indicies de las conversaciones del historial cargado
        print(f"{i}. {conv[0][0][:50]}...")  # muestra inicio del primer mensaje

    indice = int(input("Elige el número de la conversación que quieres resumir: "))
    
    # Asegurarse de que el índice esté dentro de los límites del historial
    if indice < 0 or indice >= len(historialCargado):
        print("Índice no válido.")
        return


    conversacion = []  # Lista vacía donde se guardarán todos los mensajes con estructura tipo(role/user-content)

    bloque = historialCargado[indice]  # Obtiene solo el bloque de la conversación seleccionada
    for par in bloque:  # Recorrer cada par(Pregunta/Respuesta) dentro del bloque
        if isinstance(par, list) and len(par) == 2:  # Revisar que cada par(Pregunta/Respuesta) sea una lista con dos elementos
            conversacion.append({"role": "user", "content": par[0]})  # Agrega el mensaje del usuario 
            conversacion.append({"role": "assistant", "content": par[1]})  # Agrega la respuesta del asistente

    # Agregar la instrucción de resumen como última entrada
    conversacion.append({
        "role": "user",
        "content": "Resume esta conversación en un máximo de 50 palabras."
    })
    try:
        resp = requests.post(URL_PHP, json={"messages": conversacion})  #Se envía la conversación
        resumen = resp.json()["choices"][0]["message"]["content"]   # Obtiene el texto del resumen desde la respuesta de la API
        print(resumen)
        return resumen
    except Exception as e:
        return f"Error al generar el resumen: {e}"
    

    

