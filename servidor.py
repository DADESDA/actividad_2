# servidor.py - Servidor básico para servir la página web

import http.server
import socketserver
import os

# Puerto donde correrá el servidor
PUERTO = 8000

# Cambiar al directorio donde están los archivos
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Configurar el servidor
Handler = http.server.SimpleHTTPRequestHandler

print(f"🍽️  Servidor FoodOrder corriendo en: http://localhost:{PUERTO}")
print("Para detenerlo presiona Ctrl + C")

# Iniciar el servidor
with socketserver.TCPServer(("", PUERTO), Handler) as httpd:
    httpd.serve_forever()