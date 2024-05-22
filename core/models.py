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


class RetornoFormulario:
    @staticmethod
    def get_tabela():
        tabelas = ChamadaApi.consultar_tabela()
        form_format = [
            (tabela['Codigo'], tabela['Mes']) for tabela in tabelas
        ]
        return form_format

    @staticmethod
    def get_lista_marcas(tabela: int):
        lista_marcas = ChamadaApi.consultar_marcas(tabela, 1)
        form_format = [
            (item['Value'], item['Label']) for item in lista_marcas
        ]
        return form_format

    @staticmethod
    def get_veiculos(tabela: int, marca: int):
        lista_carros = []
        tipo_veiculo = 1
        modelos_marca = ChamadaApi.consultar_veiculos_marca(tabela, tipo_veiculo, marca)

        for carro in modelos_marca['Modelos']:
            lista_carros.append(carro)

        form_format = [
            (item['Value'], item['Label']) for item in lista_carros
        ]
        return form_format

    @staticmethod
    def get_anos_veiculo(tabela: int, marca: int, veiculo: int):
        tipo_veiculo = 1
        veiculos_anos = ChamadaApi.consultar_anos_veiculo(tabela, tipo_veiculo, marca, veiculo)

        lista_anos = []
        for modelo in veiculos_anos:
            ano = modelo['Value'].split("-")[0]
            combustivel = modelo['Value'].split("-")[1]
            modelo.update({'Ano': ano})
            modelo.update({'TipoCombustivel': combustivel})
            lista_anos.append(modelo)

        form_format = [
            (item['Value'], item['Label']) for item in veiculos_anos
        ]
        return form_format, veiculos_anos

    @staticmethod
    def get_versoes_veiculo(tabela: int, marca: int, ano: str, combustivel: int, ano_modelo: int):
        tipo_veiculo = 1
        modelos = ChamadaApi.consultar_modelo(tabela, tipo_veiculo, marca, ano, combustivel, ano_modelo)

        form_format = [
            (item['Value'], item['Label']) for item in modelos
        ]

        return form_format

    @staticmethod
    def consulta_valor(tabela: int, marca: int, ano: str, tipo_combustivel: int, ano_modelo: int, codigo_modelo: int):
        tipo_consulta = "tradicional"
        tipo_veiculo = 1
        consulta = ChamadaApi.consulta_valor(tabela, tipo_veiculo, marca, ano, tipo_combustivel, ano_modelo,
                                             codigo_modelo, tipo_consulta)
        valor_formatado = int(consulta['Valor'].replace('.', '').replace('R$', '').replace(',00', ''))
        form_format = (consulta['CodigoFipe'], valor_formatado, consulta['MesReferencia'])

        return form_format
