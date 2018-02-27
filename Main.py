# -*- encoding: utf-8 -*-

import zipfile

import bs4
import requests

from Model.Sorteio import Sorteio

FILE_PATH = "resultados.zip"
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

table = soup.find_all('table')

trs = soup.find_all('tr')
del trs[0]

sorteios = []

skips = 0


def create_sorteio(tr):
    sk = 0
    attr = [td.text for td in tr if td != "\n"]

    data = {
        'concurso': attr[0],
        'data_sorteio': attr[1],
        'dezena_1': attr[2],
        'dezena_2': attr[3],
        'dezena_3': attr[4],
        'dezena_4': attr[5],
        'dezena_5': attr[6],
        'dezena_6': attr[7],
        'arrecadacao_total': attr[8],
        'ganhadores_sena': attr[9],
        'cidades': attr[10],
        'ufs': attr[11],
        'rateio_sena': attr[12],
        'ganhadores_quina': attr[13],
        'rateio_quina': attr[14],
        'ganhadores_quadra': attr[15],
        'rateio_quadra': attr[16],
        'acumulado': attr[17],
        'valor_acumulado': attr[18],
        'estimativa_premio': attr[19],
        'acumulado_mega_da_virada': attr[20]
    }

    if int(attr[9]) > 1:
        sk = int(attr[9]) - 1

    return Sorteio(data=data), sk


def get_sorteio(id_concurso):
    s = [sorteio for sorteio in sorteios if sorteio.get_concurso() == id_concurso]
    return s[0] if len(s) > 0 else None


def remove_sorteio(id_concurso):
    s = get_sorteio(id_concurso)
    sorteios.remove(s) if s is not None else None


def exists_sorteio(id_concurso):
    return True if get_sorteio(id_concurso) else False


for tr in trs:

    if skips > 0:

        if len(tr) > 3:
            s, skips = create_sorteio(tr)
            sorteios.append(s)

        else:
            skips -= 1

            print('-------------')
            cidade_uf = [td.text for td in tr if td != "\n"]
            if len(cidade_uf) > 2:
                print('shit')
            print('-------------')

    else:

        s, skips = create_sorteio(tr)
        sorteios.append(s)

print(str(len(sorteios)) + ' importados.')
print(exists_sorteio("2018"))
print(str(len(sorteios)) + ' importados.')

# print(get_sorteio("2017").to_json())
