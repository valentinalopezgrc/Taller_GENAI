# Taller GENAI - Aplicaciones con Gemini

Este repositorio contiene el desarrollo de tres ejercicios prácticos enfocados en el uso de modelos de Inteligencia Artificial generativa utilizando Gemini API y Python.

El objetivo es comprender cómo integrar IA en aplicaciones reales mediante inferencia, procesamiento de texto y sistemas conversacionales.

---

## Tecnologías utilizadas

- Python 3  
- Gemini API (Google GenAI)  
- python-dotenv  
- Entornos virtuales (venv)  

---

## Configuración del entorno

### 1. Clonar repositorio

```bash
git clone https://github.com/valentinalopezgrc/Taller_GENAI.git
cd Taller_GENAI
```

### 2. Crear entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install google-genai python-dotenv
```

### 4. Configurar API KEY

Crear un archivo `.env` en la raíz del proyecto:

```env
GENAI_API_KEY=tu_api_key_aqui
```

---

## Ejercicios

## Ejercicio 1: Concepto de Inferencia en IA

**Script:** `ejercicio_1.py`

Explica qué es la inferencia en inteligencia artificial utilizando Gemini.

### Ejecutar

```bash
python3 ejercicio_1.py
```

---

### Ejercicio 1: Concepto de Inferencia en IA

![Ejercicio 1](Ejercicio%201.png)


## Ejercicio 2: Procesador de Textos Inteligente

**Script:** `ejercicio_2.py`

### Función

```python
procesar_articulo(texto, tarea)
```

### Permite

- Generar un resumen ejecutivo  
- Reescribir texto con tono formal y profesional  

La IA actúa como un editor editorial profesional.

### Ejecutar

```bash
python3 ejercicio_2.py
```

Luego ingresar:

- el texto  
- la tarea: `resumir` o `profesionalizar`

---

![Resumen Ejecutivo](Ejercicio%202%20-%20Resumen%20Ejecutivo.png)

![Texto formal](Ejercicio%202%20-%20Texto%20formal.png)

## Ejercicio 3: Chat de Soporte con Historial (Few-Shot)

**Script:** `ejercicio_3.py`

Simula un chat de soporte para una tienda tecnológica.

### Características

- La IA actúa como vendedor amable  
- Incluye historial precargado (few-shot)  
- Proporciona especificaciones técnicas  
- Conversación continua hasta escribir **finalizar**

### Ejecutar

```bash
python3 ejercicio_3.py
```

### Ejemplos de preguntas

- ¿Cuánta RAM necesita un PC gamer?  
- ¿Qué audífonos tienen mejor sonido envolvente?

---

![Ejercicio 3](Ejercicio%203.png)

## Autor

Laura Valentina López García  
Estudiante de Ingeniería de Sistemas
