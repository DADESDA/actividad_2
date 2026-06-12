
import http.server
import socketserver
import os


PUERTO = 8000


os.chdir(os.path.dirname(os.path.abspath(__file__)))


Handler = http.server.SimpleHTTPRequestHandler

print(f"🍽️  Servidor FoodOrder corriendo en: http://localhost:{PUERTO}")
print("Para detenerlo presiona Ctrl + C")


with socketserver.TCPServer(("", PUERTO), Handler) as httpd:
    httpd.serve_forever()