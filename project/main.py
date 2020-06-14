#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Modulo para manejar HTML
import requests
# Importar Beautifulsoup
from bs4 import BeautifulSoup

# URL para hacer webscrapping
URL = 'http://econpy.pythonanywhere.com/ex/001.html'

if __name__ == '__main__':
    response = requests.get(URL)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')

        # print(soup.prettify())
        print(soup.head)
        print(type(soup.head))
