#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Modulo para manejar HTML
import requests
# Importar Beautifulsoup
from bs4 import BeautifulSoup

# URL para hacer webscrapping
URL = 'http://econpy.pythonanywhere.com/ex/001.html'

if __name__ == '__main__':
    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        # Iteracion para encontrar cada elemento.
        # Usamos el primer atributo para buscar una etiqueta
        # Como segundo argumento, colocamos los atributos para ser
        # puntual en la extracion de los elementos
        for element in soup.find_all('div', {'title': 'buyer-info'}): # []

            div = element.find('div') # None
            span = element.find('span')
            print(div.text, span.getText())


# if __name__ == '__main__':
#     response = requests.get(URL)
#
#     if response.status_code == 200:
#         content = response.text
#
#         soup = BeautifulSoup(content, 'html.parser')
#
#         # print(soup.prettify())
#         print(soup.head)
#         print(type(soup.head.title))
