from UsrManagement import *
import json


carpeta_usr = "usr" #carpeta para guardar los usuarios
carpeta_conv = "conv" #carpeta para guardar las conversaciones


def escribirArchivosConv(nombreUsr, conversacion):
    """Método que escribe las conversaciones en los archivos que estan en la carpeta de conversaciones
    Args:
        nombreUsr (str): Nombre de usuario del inicio de sesión
        mensaje (str): Mensaje que se escribio en la conversación
        respuesta (str): Respuesta que dio chatgpt ante el mensaje
    """

    rutaArchivo = f"conv\\{nombreUsr}Historial.json"  # La ruta de la conversación estará en un json


    # Crear la carpeta si no existe
    if os.path.exists(rutaArchivo):
        with open(rutaArchivo, "r", encoding="utf-8") as archivo:
            historialConv = json.load(archivo)
    else:
        historialConv = []#si no existe crea una lista vacía para almacenar el historial de conversacion



    # Convertir el historial en una lista de diccionarios con formato {"usuario": ..., "chatgpt": ...}
    conver=[]
    for mensaje in range(1, len(conversacion), 2):  # Se salta el primer mensaje del "system"
        if mensaje + 1 < len(conversacion):  # Asegurarse de que hay una respuesta de ChatGPT
           
            conver.append([conversacion[mensaje]["content"], 
                           conversacion[mensaje + 1]["content"]])

    if conver:
        historialConv.append(conver)  # Se guarda la conversación agrupada
        conver.clear
           



    # Guardar en formato JSON
    with open(rutaArchivo, "w", encoding="utf-8") as archivo:
        json.dump(historialConv, archivo, ensure_ascii=False, indent=4)

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
        historial = json.load(archivo)

    # Convertir el historial en formato compatible con la API
    conversacion = [{"role": "system", "content": historial[0][0][0]}]  # Mensaje del sistema

    for bloque in historial:
        for i in range(1, len(bloque)):  # Omitimos el mensaje del sistema en los bloques siguientes
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

    with open(rutaArchivo, "r", encoding="utf-8") as archivo:
        historialFormateado = json.load(archivo)

    print("\n--- HISTORIAL DE CONVERSACIÓN ---")
    for conversacion, listaConversaciones in enumerate(historialFormateado):
        print(f"\n ---Conversación {conversacion + 1}:---")
        for mensaje in listaConversaciones:
                print(f"\n Usuario: {mensaje[0]}".rjust)
                print(f" ChatGPT: {mensaje[1]}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n--- FIN DEL HISTORIAL ---")