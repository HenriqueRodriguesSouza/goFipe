"""APIs de consulta de veiculos na tabela FIPE para python, seguindo o exemplo documentado do @giovanigenerali"""
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# obs gerais:
# 1 = carros, 2 = motos, 3 = caminhões
# Para obter o valor de codigoTipoCombustivel e anoModelo, devemos fazer um parse(dividir o valor) do retorno ano,
# exemplo (2011-1), significa: codigoTipoCombustivel=1 e anoModelo=2011

class ChamadaApi:
    @staticmethod
    def consultar_tabela():
        """consulta as tabelas de referência, disponiveis cada mês"""
        url = "https://veiculos.fipe.org.br/api/veiculos/ConsultarTabelaDeReferencia"

        headers = {
            "Host": "veiculos.fipe.org.br",
            "Referer": "https://veiculos.fipe.org.br",
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers, verify=False, timeout=20)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def consultar_marcas(tabela, tipo_veiculo):
        """consulta as marcas dos veículos disponiveis em uma tabela de referência"""
        url = "https://veiculos.fipe.org.br/api/veiculos/ConsultarMarcas"

        headers = {
            "Host": "veiculos.fipe.org.br",
            "Referer": "https://veiculos.fipe.org.br",
            "Content-Type": "application/json",
        }

        body = {
            "codigoTabelaReferencia": tabela,
            "codigoTipoVeiculo": tipo_veiculo
        }
        response = requests.post(url, headers=headers, json=body, verify=False, timeout=20)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def consultar_veiculos_marca(tabela, tipo_veiculo, marca):
        """consulta os modelos de veículos disponiveis para uma marca em uma tabela de referência"""
        url = "https://veiculos.fipe.org.br/api/veiculos/ConsultarModelos"

        headers = {
            "Host": "veiculos.fipe.org.br",
            "Referer": "https://veiculos.fipe.org.br",
            "Content-Type": "application/json",
        }

        body = {
            "codigoTabelaReferencia": tabela,
            "codigoTipoVeiculo": tipo_veiculo,
            "codigoMarca": marca
        }
        response = requests.post(url, headers=headers, json=body, verify=False, timeout=20)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def consultar_anos_veiculo(tabela, tipo_veiculo, marca, veiculo):
        """consulta os anos do modelo de veículo especifico disponiveis em uma tabela de referência"""
        url = "https://veiculos.fipe.org.br/api/veiculos/ConsultarAnoModelo"

        headers = {
            "Host": "veiculos.fipe.org.br",
            "Referer": "https://veiculos.fipe.org.br",
            "Content-Type": "application/json",
        }

        body = {
            "codigoTabelaReferencia": tabela,
            "codigoTipoVeiculo": tipo_veiculo,
            "codigoMarca": marca,
            "codigoModelo": veiculo,
        }

        response = requests.post(url, headers=headers, json=body, verify=False, timeout=20)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def consultar_modelo(tabela, tipo_veiculo, marca, ano, combustivel, ano_modelo):
        """retorna todos os veículo de uma marca do ano especifico em uma tabela de referência"""
        url = "https://veiculos.fipe.org.br/api/veiculos/ConsultarModelosAtravesDoAno"

        headers = {
            "Host": "veiculos.fipe.org.br",
            "Referer": "https://veiculos.fipe.org.br",
            "Content-Type": "application/json",
        }

        body = {
            "codigoTabelaReferencia": tabela,
            "codigoTipoVeiculo": tipo_veiculo,
            "codigoMarca": marca,
            "ano": ano,
            "codigoTipoCombustivel": combustivel,
            "anoModelo": ano_modelo

        }

        response = requests.post(url, headers=headers, json=body, verify=False, timeout=20)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def consulta_valor(tabela, tipo_veiculo, marca, ano, tipo_combustivel, ano_modelo, codigo_modelo, tipo_consulta):
        """retorna o valor de um veículo especifico em uma tabela de referência"""
        url = "https://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros"

        headers = {
            "Host": "veiculos.fipe.org.br",
            "Referer": "https://veiculos.fipe.org.br",
            "Content-Type": "application/json",
        }

        body = {
            "codigoTabelaReferencia": tabela,
            "codigoTipoVeiculo": tipo_veiculo,
            "codigoMarca": marca,
            "ano": ano,
            "codigoTipoCombustivel": tipo_combustivel,
            "anoModelo": ano_modelo,
            "codigoModelo": codigo_modelo,
            "tipoConsulta": tipo_consulta
        }

        response = requests.post(url, headers=headers, json=body, verify=False, timeout=20)
        if response.status_code == 200:
            return response.json()
        else:
            return None