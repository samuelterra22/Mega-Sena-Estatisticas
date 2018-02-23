# -*- encoding: utf-8 -*-

import zipfile

import re
import requests
from bs4 import BeautifulSoup
import bs4, sys

STORAGE_PATH = "/tmp/mega"
FILENAME = "resultados.zip"
FILE_PATH = FILENAME
INSIDE_FILENAME = "d_megasc.htm"
URL = "http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_mgsasc.zip"

print("[-] Baixano o arquivo de resultados...")

f = requests.get(URL)

with open(FILE_PATH, "wb") as myzip:
    myzip.write(f.content)
    myzip.close()

print("[-] Pronto! Extraindo...")

if zipfile.is_zipfile(FILE_PATH):
    zip = zipfile.ZipFile(FILE_PATH)
    zip.extract(INSIDE_FILENAME)

print("[-] Abrindo arquivo para buscar os resultados...")

with open("d_megasc.htm", 'r', encoding="utf8", errors='ignore') as f:
    content = f.read()

soup = bs4.BeautifulSoup(content, "lxml")

# for node in soup.findAll('html'):
#     print(node.findAll(text=True))

for i, tr in enumerate(soup.find_all('table')):
    for td in tr:
        print(td)
