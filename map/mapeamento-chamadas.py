'''Mapeamento das APIs de consulta de veiculos na tabela FIPE para python, seguindo o exemplo documentado do @giovanigenerali'''
import requests

# obs gerais:
# 1 = carros, 2 = motos, 3 = caminhões
# Para obter o valor de codigoTipoCombustivel e anoModelo, devemos fazer um parse(dividir o valor) do retorno ano, exemplo (2011-1), deve ficar: codigoTipoCombustivel=1 e anoModelo=2011  


def consultar_tabela():
    '''consulta as tabelas de referência, disponiveis cada mês'''
    url = "https://veiculos.fipe.org.br/api/veiculos/ConsultarTabelaDeReferencia"

    headers = {
        "Host": "veiculos.fipe.org.br",
        "Referer": "https://veiculos.fipe.org.br",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, verify=False, timeout=20)
    return response

#consultar_tabela()

def consultar_marcas(tabela=231, veiculo=1):
    '''consulta as marcas dos veículos disponiveis em uma tabela de referência'''
    url = "http://veiculos.fipe.org.br/api/veiculos/ConsultarMarcas"

    headers = {
        "Host": "veiculos.fipe.org.br",
        "Referer": "http://veiculos.fipe.org.br",
        "Content-Type": "application/json",
    }

    body = {
        "codigoTabelaReferencia": tabela,
        "codigoTipoVeiculo": veiculo
    }
    response = requests.post(url, headers=headers, json=body, verify=False, timeout=20)
    return response

#consultar_marcas(231, 1)

def consultar_veiculos_marca(tabela, tipo_veiculo, marca):
    '''consulta os modelos de veículos disponiveis para uma marca em uma tabela de referência'''
    url = "http://veiculos.fipe.org.br/api/veiculos/ConsultarModelos"

    headers = {
        "Host": "veiculos.fipe.org.br",
        "Referer": "http://veiculos.fipe.org.br",
        "Content-Type": "application/json",
    }

    body = {
        "codigoTabelaReferencia": tabela,
        "codigoTipoVeiculo": tipo_veiculo,
        "codigoMarca": marca
    }
    response = requests.post(url, headers=headers, json=body, verify=False, timeout=20)
    return response

#consultar_veiculos_marca(231, 1, 26)

def consultar_anos_veiculo(tabela, tipo_veiculo, marca, modelo):
    '''consulta os anos do modelo de veículo especifico disponiveis em uma tabela de referência'''
    url = "http://veiculos.fipe.org.br/api/veiculos/ConsultarAnoModelo"

    headers = {
        "Host": "veiculos.fipe.org.br",
        "Referer": "http://veiculos.fipe.org.br",
        "Content-Type": "application/json",
    }

    body = {
        "codigoTabelaReferencia": tabela,
        "codigoTipoVeiculo": tipo_veiculo,
        "codigoMarca": marca,
        "codigoModelo": modelo,
    }

    response = requests.post(url, headers=headers, json=body, verify=False, timeout=20)
    return response
    
#consultar_anos_veiculo(231, 1, 26, 4403)

def consultar_modelo(tabela, tipo_veiculo, marca, ano, combustivel, ano_modelo):
    '''retorna todos os veículo de uma marca do ano especifico em uma tabela de referência'''
    url = "http://veiculos.fipe.org.br/api/veiculos/ConsultarModelosAtravesDoAno"

    headers = {
        "Host": "veiculos.fipe.org.br",
        "Referer": "http://veiculos.fipe.org.br",
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
    return response
    
#consultar_modelo(231, 1, 26, "2011-2", 1, 2011)

def consulta_valor(tabela, tipo_veiculo, marca, ano, tipo_combustivel, ano_modelo, codigo_modelo, tipo_consulta):
    '''retorna o valor de um veículo especifico em uma tabela de referência'''
    url = "http://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros"

    headers = {
        "Host": "veiculos.fipe.org.br",
        "Referer": "http://veiculos.fipe.org.br",
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
    return response

#consulta_valor(231, 1, 26, "2011-2", 1, 2011, 4403, "tradicional")

