# Ejercicio 2: Resumir y profesionalizar artículos con Gemini-2.5-flash
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Carga las variables de entorno desde el archivo .env
load_dotenv()  
API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar el cliente de GenAI con la clave de API
client = genai.Client(api_key=API_KEY)

# Configuración común para ambas tareas
configuration = types.GenerateContentConfig(
    system_instruction="""Eres un Editor Editorial de prestigio. Tu estilo es claro, formal, técnico y profesional."""
)

# Función para procesar el artículo según la tarea seleccionada
def procesar_articulo(texto, tarea):
    if tarea == "resumir":
        instruccion = "Realiza un resumen ejecutivo claro y conciso del siguiente texto."
    elif tarea == "profesionalizar":
        instruccion = "Reescribe el texto con tono formal, técnico y profesional."
    else:
        return "Tarea no válida. Usa 'resumir' o 'profesionalizar'."

    prompt = f"{instruccion}\n\nTexto:\n{texto}"

    respuesta = client.models.generate_content(
        model="gemini-2.5-flash",
        config=configuration,
        contents=prompt
    )

    return respuesta.text

# Ejemplo de uso
if __name__ == "__main__":
    texto = input("Pega el texto: ")
    tarea = input("Escribe la tarea (resumir/profesionalizar): ")

    resultado = procesar_articulo(texto, tarea)
    print("\nResultado:\n")
    print(resultado)