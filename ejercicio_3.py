# Ejercicio 3: Chat de soporte para tienda tecnológica
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar cliente
client = genai.Client(api_key=API_KEY)

# Configuración del modelo
configuration = types.GenerateContentConfig(
    system_instruction="""
Eres un vendedor amable y experto de una tienda de tecnología.
Respondes de forma clara, útil y profesional.
Ofreces especificaciones técnicas y ayudas al cliente a elegir.
"""
)

# Historial few-shot (ejemplos de interacción)
history = [
    types.Content(
        role="user",
        parts=[types.Part(text="¿Qué características tiene el iPhone 17?")]
    ),
    types.Content(
        role="model",
        parts=[types.Part(text="El iPhone 17 cuenta con pantalla Super Retina XDR de 6.1 pulgadas, chip A17 Pro, cámara de 48 MP, USB-C y excelente rendimiento energético.")]
    ),
    types.Content(
        role="user",
        parts=[types.Part(text="¿Cuánta memoria tiene el Samsung Galaxy S25?")]
    ),
    types.Content(
        role="model",
        parts=[types.Part(text="El Samsung Galaxy S25 incluye 8 GB de RAM y opciones de almacenamiento de 128 GB, 256 GB y 512 GB, con procesador Snapdragon 8 Gen 2.")]
    ),
]

# Crear chat con historial precargado
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=configuration,
    history=history
)

print("🛒 Chat de Soporte - Tienda Tecnológica")
print("Escribe 'finalizar' para terminar.\n")

while True:
    pregunta = input("Cliente: ")

    if pregunta.lower() == "finalizar":
        print("Vendedor: ¡Gracias por visitarnos! 😊")
        break

    respuesta = chat.send_message(pregunta)
    print(f"\nVendedor: {respuesta.text}\n")