# -*- coding: utf-8 -*-
class Sorteio(object):
    """
    Esta classe representa um Sorteio realizado.
    """

    def __init__(self, data):
        """
        Contrutor de 'Sorteio'.

        :param data: Dicionario com as informacoes do Sorteio.

        data['concurso']: Identificador do concurso referente ao Sorteio.
        data['data_sorteio']: Data de realizacao do Sorteio.
        data['dezena_1']: Primeira dezena do Sorteio.
        data['dezena_2']: Segunada dezena do Sorteio.
        data['dezena_3']: Terceira dezena do Sorteio.
        data['dezena_4']: Quarta dezena do Sorteio.
        data['dezena_5']: Quinta dezena do Sorteio.
        data['dezena_6']: Sexta dezena do Sorteio.
        data['arrecadacao_total']: Arrecadacao total do Sorteio.
        data['ganhadores_sena']: Quantidade dos ganhadores do Sorteio.
        data['cidade']: Cidade dos ganhadores do Sorteio.
        data['uf']: UF dos ganhadores dos Sorteio.
        data['rateio_sena']: Rateio do Sena.
        data['ganhadores_quina']: Quantidade de ganhadores da Quina.
        data['rateio_quina']: Rateio da Quina.
        data['ganhadores_quadra']: Quantidade de ganhadores da Quadra.
        data['rateio_quadra']: Rateio da Quadra.
        data['acumulado']: Flag informando se o valor ficou acumulado.
        data['valor_acumulado']: Valor acumulado.
        data['estimativa_premio']: Estimativa do valor do premio.
        data['acumulado_mega_da_virada']: Valor acumulado da Mega da Virada.
        """

        self._concurso = data['concurso']
        self._data_sorteio = data['data_sorteio']
        self._dezena_1 = data['dezena_1']
        self._dezena_2 = data['dezena_2']
        self._dezena_3 = data['dezena_3']
        self._dezena_4 = data['dezena_4']
        self._dezena_5 = data['dezena_5']
        self._dezena_6 = data['dezena_6']
        self._arrecadacao_total = data['arrecadacao_total']
        self._ganhadores_sena = data['ganhadores_sena']

        self._cidade = [] if data['cidade'] is None or data['cidade'] == '' or data['cidade'] == '&nbsp' else data[
            'cidade']

        self._uf = [] if data['uf'] is None or data['uf'] == '' or data['uf'] == '&nbsp' else data['uf']
        self._rateio_sena = data['rateio_sena']
        self._ganhadores_quina = data['ganhadores_quina']
        self._rateio_quina = data['rateio_quina']
        self._ganhadores_quadra = data['ganhadores_quadra']
        self._rateio_quadra = data['rateio_quadra']
        self._acumulado = data['acumulado']
        self._valor_acumulado = data['valor_acumulado']
        self._estimativa_premio = data['estimativa_premio']
        self._acumulado_mega_da_virada = data['acumulado_mega_da_virada']

    def get_concurso(self):
        """
        Metodo responsavel por retornar o concurso do Sorteio.
        :return: Inteiro referente ao concurso do Sorteio.
        """
        return self._concurso

    def set_concurso(self, concurso):
        """
        Metodo responsavel por setar o concurso do Sorteio.
        :return: None.
        """
        self._concurso = concurso

    def get_data_sorteio(self):
        """
        Metodo responsavel por retornar a data do Sorteio.
        :return: Data de realizacao do Sorteio.
        """
        return self._data_sorteio

    def set_data_sorteio(self, data_sorteio):
        """
        Metodo responsavel por setar a data do Sorteio.
        :return: None.
        """
        self._data_sorteio = data_sorteio

    def get_dezena_1(self):
        """
        Metodo responsavel por retornar a dezena 1 do Sorteio.
        :return: Dezena 1 do Sorteio.
        """
        return self._dezena_1

    def set_dezena_1(self, dezena_1):
        """
        Metodo responsavel por setar a dezena 1 do Sorteio.
        :return: None.
        """
        self._dezena_1 = dezena_1

    def get_dezena_2(self):
        """
        Metodo responsavel por retornar a dezena 2 do Sorteio.
        :return: Dezena 2 do Sorteio.
        """
        return self._dezena_2

    def set_dezena_2(self, dezena_2):
        """
        Metodo responsavel por setar a dezena 2 do Sorteio.
        :return: None.
        """
        self._dezena_2 = dezena_2

    def get_dezena_3(self):
        """
        Metodo responsavel por retornar a dezena 3 do Sorteio.
        :return: Dezena 3 do Sorteio.
        """
        return self._dezena_3

    def set_dezena_3(self, dezena_3):
        """
        Metodo responsavel por setar a dezena 3 do Sorteio.
        :return: None.
        """
        self._dezena_3 = dezena_3

    def get_dezena_4(self):
        """
        Metodo responsavel por retornar a dezena 4 do Sorteio.
        :return: Dezena 4 do Sorteio.
        """
        return self._dezena_4

    def set_dezena_4(self, dezena_4):
        """
        Metodo responsavel por setar a dezena 4 do Sorteio.
        :return: None.
        """
        self._dezena_4 = dezena_4

    def get_dezena_5(self):
        """
        Metodo responsavel por retornar a dezena 5 do Sorteio.
        :return: Dezena 5 do Sorteio.
        """
        return self._dezena_5

    def set_dezena_5(self, dezena_5):
        """
        Metodo responsavel por setar a dezena 5 do Sorteio.
        :return: None.
        """
        self._dezena_5 = dezena_5

    def get_dezena_6(self):
        """
        Metodo responsavel por retornar a dezena 6 do Sorteio.
        :return: Dezena 6 do Sorteio.
        """
        return self._dezena_6

    def set_dezena_6(self, dezena_6):
        """
        Metodo responsavel por setar a dezena 6 do Sorteio.
        :return: None.
        """
        self._dezena_6 = dezena_6

    def get_arrecadacao_total(self):
        """
        Metodo responsavel por retornar a arrecadacao total do Sorteio.
        :return: Arrecadacao total do Sorteio.
        """
        return self._arrecadacao_total

    def set_arrecadacao_total(self, arrecadacao_total):
        """
        Metodo responsavel por setar a arrecadacao total do Sorteio.
        :return: None.
        """
        self._arrecadacao_total = arrecadacao_total

    def get_ganhadores_sena(self):
        """
        Metodo responsavel por retornar os ganhadores da sena do Sorteio.
        :return: Ganhadores da sena do Sorteio.
        """
        return self._ganhadores_sena

    def set_ganhadores_sena(self, ganhadores_sena):
        """
        Metodo responsavel por setar os ganhadores da sena do Sorteio.
        :return: None.
        """
        self._ganhadores_sena = ganhadores_sena

    def get_cidade(self):
        """
        Metodo responsavel por retornar as cidades do Sorteio.
        :return: Cidade do Sorteio.
        """
        return self._ganhadores_sena

    def set_cidade(self, cidade):
        """
        Metodo responsavel por setar as cidades do Sorteio.
        :return: None.
        """
        self._cidade = cidade

    def get_uf(self):
        """
        Metodo responsavel por retornar os UFs do Sorteio.
        :return: UFs do Sorteio.
        """
        return self._ganhadores_sena

    def set_uf(self, uf):
        """
        Metodo responsavel por setar os UFs do Sorteio.
        :return: None.
        """
        self._uf = uf

    def get_rateio_sena(self):
        """
        Metodo responsavel por retornar o rateio da sena do Sorteio.
        :return: Rateio da sena do Sorteio.
        """
        return self._rateio_sena

    def set_rateio_sena(self, rateio_sena):
        """
        Metodo responsavel por setar o rateio da sena do Sorteio.
        :return: None.
        """
        self._rateio_sena = rateio_sena

    def get_ganhadores_quina(self):
        """
        Metodo responsavel por retornar os ganhadores da quina do Sorteio.
        :return: Rateio da sena do Sorteio.
        """
        return self._ganhadores_quina

    def set_ganhadores_quina(self, ganhadores_quina):
        """
        Metodo responsavel por setar os ganhadores da quina do Sorteio.
        :return: None.
        """
        self._ganhadores_quina = ganhadores_quina

    def get_rateio_quina(self):
        """
        Metodo responsavel por retornar o rateio da quina do Sorteio.
        :return: Rateio da quina do Sorteio.
        """
        return self._rateio_quina

    def set_rateio_quina(self, rateio_quina):
        """
        Metodo responsavel por setar o rateio da sena do Sorteio.
        :return: None.
        """
        self._rateio_quina = rateio_quina

    def get_ganhadores_quadra(self):
        """
        Metodo responsavel por retornar os ganhadores da quadra do Sorteio.
        :return: Rateio da sena do Sorteio.
        """
        return self._ganhadores_quadra

    def set_ganhadores_quadra(self, ganhadores_quadra):
        """
        Metodo responsavel por setar os ganhadores da quadra do Sorteio.
        :return: None.
        """
        self._ganhadores_quadra = ganhadores_quadra

    def get_rateio_quadra(self):
        """
        Metodo responsavel por retornar o rateio da quadra do Sorteio.
        :return: Rateio da quadra do Sorteio.
        """
        return self._rateio_quadra

    def set_rateio_quadra(self, rateio_quadra):
        """
        Metodo responsavel por setar o rateio da sena do Sorteio.
        :return: None.
        """
        self._rateio_quadra = rateio_quadra

    def get_acumulado(self):
        """
        Metodo responsavel por retornar o acumulado do Sorteio.
        :return: Acumulado do Sorteio.
        """
        return self._acumulado

    def set_acumulado(self, acumulado):
        """
        Metodo responsavel por setar o acumulado do Sorteio.
        :return: None.
        """
        self._acumulado = acumulado

    def get_valor_acumulado(self):
        """
        Metodo responsavel por retornar o valor acumulado do Sorteio.
        :return: Valor acumulado do Sorteio.
        """
        return self._acumulado

    def set_valor_acumulado(self, valor_acumulado):
        """
        Metodo responsavel por setar o valor acumulado do Sorteio.
        :return: None.
        """
        self._valor_acumulado = valor_acumulado

    def get_estimativa_premio(self):
        """
        Metodo responsavel por retornar a estimativa do premio do Sorteio.
        :return: A estimativa do premio do Sorteio.
        """
        return self._acumulado

    def set_estimativa_premio(self, estimativa_premio):
        """
        Metodo responsavel por setar a estimativa do premio do Sorteio.
        :return: None.
        """
        self._estimativa_premio = estimativa_premio

    def get_acumulado_mega_da_virada(self):
        """
        Metodo responsavel por retornar o acumulado da mega da virada do Sorteio.
        :return: O acumulado da mega da virada do Sorteio.
        """
        return self._acumulado

    def set_acumulado_mega_da_virada(self, acumulado_mega_da_virada):
        """
        Metodo responsavel por setar o acumulado da mega da virada do Sorteio.
        :return: None.
        """
        self._acumulado_mega_da_virada = acumulado_mega_da_virada
