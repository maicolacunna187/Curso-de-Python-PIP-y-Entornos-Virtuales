"""
--- Guía de Instalación de Librerías con PIP (Formato Actual) ---

Paso 1: Instalar el paquete para crear entornos virtuales.
(Este paso es necesario en sistemas operativos modernos como Ubuntu para evitar errores de permisos).
Comando:  sudo apt install python3.12-venv

Paso 2: Crear el entorno virtual en tu carpeta de proyecto.
(Se crea una carpeta aislada llamada 'venv').
Comando:  python3 -m venv .venv

Paso 3: Activar el entorno virtual.
(Esto te permite instalar librerías sin afectar tu sistema).
Comando:  source .venv/bin/activate
* Después de este paso verás (venv) al inicio de tu línea de comandos.

Paso 4: Instalar la librería matplotlib.
(Ahora la librería se instalará de forma segura dentro de tu entorno virtual).
Comando: pip install matplotlib

Paso 5 (opcional): Desactivar el entorno cuando termines.
Comando: deactivate
"""