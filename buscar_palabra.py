#!/usr/bin/env python3
import cgi

# Obtener los datos del formulario
form = cgi.FieldStorage()
texto = form.getvalue("texto", "")
palabra = form.getvalue("palabra", "")

# Contar ocurrencias de la palabra en el texto
palabras = texto.lower().split()
conteo = palabras.count(palabra.lower())

# Generar página de respuesta
print("Content-type: text/html\n")
print("<!DOCTYPE html>")
print("<html lang='es'>")
print("<head>")
print("<meta charset='UTF-8'>")
print("<meta name='viewport' content='width=device-width, initial-scale=1.0'>")
print("<title>Resultado de la búsqueda</title>")
print("</head>")
print("<body>")
print("<h1>Resultado de la búsqueda</h1>")
print(f"<p>La palabra '{palabra}' se repite {conteo} veces en el texto ingresado.</p>")
print("</body>")
print("</html>")

