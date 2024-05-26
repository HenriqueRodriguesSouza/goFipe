from django import forms

from .views import *

class VeiculoForm(forms.Form):

    data_inicial = forms.ChoiceField(required=True, choices=RetornoFormulario.get_tabela(), widget = forms.Select(attrs={'hx-get': 'tabela_final', 'hx-target': '#id_data_final'}))
    data_final = forms.ChoiceField(required=True, choices="", widget=forms.Select(attrs={'hx-get':'load_marcas', 'hx-target':'#id_marca'}))
    marca = forms.ChoiceField(required=True, choices="", widget=forms.Select(attrs={'hx-get':'load_veiculos', 'hx-target':'#id_veiculo'}))
    veiculo = forms.ChoiceField(required=True, choices="", widget=forms.Select(attrs={'hx-get':'load_anos', 'hx-target':'#id_ano_veiculo'}))
    ano_veiculo = forms.ChoiceField(required=True, choices="", widget=forms.Select(attrs={'hx-get':'load_versoes', 'hx-target':'#id_versao'}))
    versao = forms.ChoiceField(required=True, choices="", widget=forms.Select(attrs={'hx-get':'criar_grafico', 'hx-target':'#myChart'}))

