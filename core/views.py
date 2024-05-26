from django.shortcuts import render
from .models import RetornoFormulario
from .form import VeiculoForm


def index(request):
    form = VeiculoForm()
    return render(request, 'index.html', {'form': form})


def tabela_final(request):
    global tabela_inicial
    tabela_inicial = request.GET.get('data_inicial')
    global tabela_selecao
    tabela_selecao = RetornoFormulario.get_tabela()
    global tabela_temp
    tabela_temp = tabela_selecao[:]
    for tabela in tabela_temp:
        if tabela[0] < int(tabela_inicial):
            tabela_selecao.remove(tabela)
    tabela_selecao.reverse()
    return render(request, "tabelas.html", {'tabelas': tabela_selecao})
def load_marcas(request):
    global tabelas_grafico
    tabelas_grafico = []
    tabela_final = request.GET.get('data_final')
    for tabela in tabela_selecao:
        if tabela[0] <= int(tabela_final):
            tabelas_grafico.append(tabela)
    marcas = RetornoFormulario.get_lista_marcas(tabela_inicial)
    return render(request, "marcas.html", {'marcas': marcas})

def load_veiculos(request):
    global marca
    marca = request.GET.get('marca')
    veiculos = RetornoFormulario.get_veiculos(tabela_inicial, marca)
    return render(request, "veiculos.html", {'veiculos': veiculos})

def load_anos(request):
    global veiculo_selecionado
    veiculo_selecionado = request.GET.get('veiculo')
    global info_anos
    anos_disponiveis, info_anos = RetornoFormulario.get_anos_veiculo(tabela_inicial, marca, veiculo_selecionado)
    return render(request, "anos.html", {'anos': anos_disponiveis})

def load_versoes(request):
    ano_selecionado = request.GET.get('ano_veiculo')

    global ano
    global anoModelo
    global combustivel
    for anos_disponiveis in info_anos:
        if anos_disponiveis['Value'] == ano_selecionado:
            ano = anos_disponiveis['Value']
            anoModelo = anos_disponiveis['Ano']
            combustivel = anos_disponiveis['TipoCombustivel']

    versoes = RetornoFormulario.get_versoes_veiculo(tabela_inicial, marca, ano, combustivel, anoModelo)
    return render(request, "versoes.html", {'versoes': versoes})


def criar_grafico(request):
    global versao_selecionado
    versao_selecionado = request.GET.get('versao')
    tabela_valores = []
    tabela_meses = []
    if request:
        for tabela in tabelas_grafico:
            info = RetornoFormulario.consulta_valor(tabela[0], marca, ano, combustivel, anoModelo, versao_selecionado)
            tabela_meses.append(info[2])
            tabela_valores.append(info[1])

    return render(request, 'grafico.html', {'labels': tabela_meses, 'valores': tabela_valores})
