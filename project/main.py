#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Modulo para expresiones regulares
import re
# Modulo para manejar HTML
import requests

# URL para hacer webscrapping
URL = 'http://econpy.pythonanywhere.com/ex/001.html'

if __name__ == '__main__':
    response = requests.get(URL)

    if response.status_code == 200:
        content = response.text

        # Expresion regular para encontrar el titulo
        regex = '<div title="buyer-name">(.+?)</div>'

        # Primer argumento: expresion regualar
        # Segundo argumento, STRING donde aplicar la expresion
        # Regresa un listado de STRINGS
        # Iteramos para poder imprimir cada uno de los elementos
        for title in re.findall(regex, content):
            print(title)
