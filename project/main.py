#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Modulo para expresiones regulares
import re
# Modulo para manejar HTML
import requests

# URL para hacer webscrapping
URL = 'http://econpy.pythonanywhere.com/ex/001.html'

if __name__ == '__main__':
    # Abrir archivo a analizar en modo lectura -r-
    with open('econpy.html', 'r') as file:
        # obtener el contenido del archivo
        content = file.read()

        # Expresion regular para encontrar el titulo
        regex = '<div title="buyer-name">(.+?)</div>'

        # Primer argumento: expresion regualar
        # Segundo argumento, STRING donde aplicar la expresion
        # Regresa un listado de STRINGS
        # Iteramos para poder imprimir cada uno de los elementos
        for title in re.findall(regex, content):
            print(title)
