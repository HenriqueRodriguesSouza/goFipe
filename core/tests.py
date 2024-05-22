#from django.test import TestCase
from models import *
import unittest
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class TestChamadaApi(unittest.TestCase):
    def test_chamadas_sucesso(self):
        #Testando o retorno dos valores das chamadas em um cenário de sucesso.
        chamada = ChamadaApi.consultar_tabela()
        self.assertEqual(chamada[0], {'Codigo': 309, 'Mes': 'maio/2024 '})

        chamada2 = ChamadaApi.consultar_marcas(231, 1)
        self.assertEqual(chamada2[0], {'Label': 'Acura', 'Value': '1'})

        chamada3 = ChamadaApi.consultar_veiculos_marca(231, 1, 26)
        self.assertEqual(chamada3['Modelos'][0], {'Label': 'Accent GLS 1.5 12V/16V Aut.', 'Value': 1286})

        chamada4 = ChamadaApi.consultar_anos_veiculo(231, 1, 26, 4403)
        self.assertEqual(chamada4[0], {'Label': '2011 Gasolina', 'Value': '2011-1'})

        chamada5 = ChamadaApi.consultar_modelo(231, 1, 26, "2011-2", 1, 2011)
        self.assertEqual(chamada5[0], {'Label': 'AZERA 3.0 V6 24V 4p Aut.', 'Value': '5726'})

        chamada6 = ChamadaApi.consulta_valor(231, 1, 26, "2011-2", 1, 2011, 4403, "tradicional")
        self.assertEqual(chamada6['Valor'], 'R$ 39.225,00')

        print("Teste dos valores retornodos nas chamadas da API realizado com sucesso")


    def test_chamadas_falha(self):
        #Testando o retorno se a chamada for feita de forma errada.
        chamada1 = ChamadaApi.consultar_marcas(500, 5)
        self.assertEqual(chamada1, {'codigo': '0', 'erro': 'nadaencontrado'})

        chamada2 = ChamadaApi.consultar_veiculos_marca(500, 4, 699)
        self.assertEqual(chamada2, {'codigo': '0', 'erro': 'nadaencontrado'})

        chamada3 = ChamadaApi.consultar_anos_veiculo(231, 1, 26, 8000)
        self.assertEqual(chamada3, {'codigo': '0', 'erro': 'nadaencontrado'})

        chamada4 = ChamadaApi.consultar_modelo(231, 1, 599, "2011-2", 1, 2011)
        self.assertEqual(chamada4, {'codigo': '0', 'erro': 'nadaencontrado'})

        chamada5 = ChamadaApi.consulta_valor(500, 7, 26, "2011-2", 1, 2077, 4403, "tradicional")
        self.assertEqual(chamada5, {'codigo': '0', 'erro': 'nadaencontrado'})

        print("Teste de retorno de erros nas chamadas da API realizado com sucesso")

    def test_itens_chamada(self):
        #Testando se a diferenca nos itens retornados.
        chamada = ChamadaApi.consultar_tabela()
        self.assertNotEqual(chamada[2], {'Codigo': 306, 'Mes': 'fevereiro/2024 '})

        chamada2 = ChamadaApi.consultar_marcas(231, 1)
        self.assertNotEqual(chamada2[2], {'Label': 'Agrale', 'Value': '2'})

        chamada3 = ChamadaApi.consultar_veiculos_marca(231, 1, 26)
        self.assertNotEqual(chamada3['Modelos'][2], {'Label': 'Accent GLS 1.5 12V/16V Mec.', 'Value': 1287})

        chamada4 = ChamadaApi.consultar_anos_veiculo(231, 1, 26, 4403)
        self.assertNotEqual(chamada4[2], {'Label': '2010 Gasolina', 'Value': '2010-1'})

        chamada5 = ChamadaApi.consultar_modelo(231, 1, 26, "2011-2", 1, 2011)
        self.assertNotEqual(chamada5[2], {'Label': 'AZERA GLS 3.3 V6 24V 4p Aut.', 'Value': '4403'})

        chamada6 = ChamadaApi.consulta_valor(231, 1, 26, "2011-2", 1, 2011, 4403, "tradicional")
        self.assertNotEqual(chamada6['Valor'], 'R$ 35.225,00')

        print("Teste de diferenca nos itens nas chamadas da API realizado com sucesso")

    def test_tempo_chamada(self):
        #exemplo usado: ChamadaApi.consulta_valor(argumentos)
        tabela = 231
        tempo_respostas = []
        while tabela < 243:
            url = "https://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros"

            headers = {
                "Host": "veiculos.fipe.org.br",
                "Referer": "https://veiculos.fipe.org.br",
                "Content-Type": "application/json",
            }

            body = {
                "codigoTabelaReferencia": tabela,
                "codigoTipoVeiculo": 1,
                "codigoMarca": 26,
                "ano": "2011-2",
                "codigoTipoCombustivel": 1,
                "anoModelo": 2011,
                "codigoModelo": 4403,
                "tipoConsulta": "tradicional"
            }

            response = requests.post(url, headers=headers, json=body, verify=False, timeout=20)
            tempo_respostas.append(response.elapsed.total_seconds())
            tabela += 1

        tempo_medio = sum(tempo_respostas) / len(tempo_respostas)
        if tempo_medio < 0.500:
            print(f'Sucesso! Tempo médio da chamada final: {round(tempo_medio, 3)} ms')
            pass
        else:
            print(f'Falha! Tempo médio da chamada final: {round(tempo_medio, 3)} ms')
            self.fail()


class TestRetornoFormulario(unittest.TestCase):
    def test_retorno_formulario(self):
        formulario = RetornoFormulario.get_tabela()
        self.assertEqual(formulario[0], (309, 'maio/2024 '))

        formulario2 = RetornoFormulario.get_lista_marcas(231)
        self.assertEqual(formulario2[0], ('1', 'Acura'))

        formulario3 = RetornoFormulario.get_veiculos(231, 26)
        self.assertEqual(formulario3[0], (1286, 'Accent GLS 1.5 12V/16V Aut.'))

        formulario4 = RetornoFormulario.get_anos_veiculo(231, 26, 4403)
        self.assertEqual(formulario4[0][0], ('2011-1', '2011 Gasolina'))

        formulario5 = RetornoFormulario.get_versoes_veiculo(231, 26, "2011-2", 1, 2011)
        self.assertEqual(formulario5[0], ('5726', 'AZERA 3.0 V6 24V 4p Aut.'))

        formulario6 = RetornoFormulario.consulta_valor(231, 26, "2011-2", 1, 2011, 4403)
        self.assertEqual(formulario6, ('015069-0', 39225, 'julho de 2018 '))

        print("Teste de retorno dos valores para o formulario realizado com sucesso")

    def test_tamanho_formulario(self):
        formulario = RetornoFormulario.get_tabela()
        self.assertEqual(len(formulario[0]), 2)

        formulario2 = RetornoFormulario.get_lista_marcas(231)
        self.assertEqual(len(formulario2[0]), 2)

        formulario3 = RetornoFormulario.get_veiculos(231, 26)
        self.assertEqual(len(formulario3[0]), 2)

        formulario4 = RetornoFormulario.get_anos_veiculo(231, 26, 4403)
        self.assertEqual(len(formulario4[0][0]), 2)

        formulario5 = RetornoFormulario.get_versoes_veiculo(231, 26, "2011-2", 1, 2011)
        self.assertEqual(len(formulario5[0]), 2)

        formulario6 = RetornoFormulario.consulta_valor(231, 26, "2011-2", 1, 2011, 4403)
        self.assertEqual(len(formulario6), 3)

        print("Teste da quantidade de informações para o formulario realizado com sucesso")

if __name__ == '__main__':
    unittest.main()