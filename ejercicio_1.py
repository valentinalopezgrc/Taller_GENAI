# Ejercicio 1: Consulta simple a Gemini-2.5-flash
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Carga las variables de entorno desde el archivo .env
load_dotenv()  
API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar el cliente de GenAI con la clave de API
client = genai.Client(api_key=API_KEY)

# Realizar la consulta simple al modelo Gemini-2.5-flash
response = client.models.generate_content(
    model="gemini-2.5-flash",
        contents="Explica qué es la inferencia en IA en menos de 50 palabras."
)
# Imprimir la respuesta del modelo
print(response.text)
