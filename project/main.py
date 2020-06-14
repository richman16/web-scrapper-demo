#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

# URL para hacer webscrapping
URL = 'http://econpy.pythonanywhere.com/ex/001.html'

if __name__ == '__main__':
    response = requests.get(URL)

    if response.status_code == 200:
        content = response.text

        # Encontrar el DIV de apertura
        regexa = '<div title="buyer-name">'
        # Encontrar el DIV de cierre
        regexb = '</div>'

        # Imprimir linea por linea el contenido de - content -
        for line in content.split('\n'):
            # Imprimir la linea donde se encuentre el DIV de apertura
            if regexa in line:
                # Seleccionamos la posicion donde inicia el texto
                start = line.find(regexa) + len(regexa)
                # Seleccionamos la posición donde termina el texto
                end = line.find(regexb)
                # Substring de la linea HTML
                title = line[start:end]
                # Imprimir el titulo
                print(title)
