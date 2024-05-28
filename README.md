# 🚗 Go Fipe 🚗

## Introdução ao Projeto Go Fipe
O projeto Go Fipe foi desenvolvido para a UC de Gestão e Qualidade de Software do professor [Alexandre de Oliveira (Montanha)](https://github.com/alexmontanha) da UniBH. Nele trabalhamos com a API oficial da Fundação Instituto de Pesquisas Econômicas, que retorna o valor da Fipe dos veículos nacionais para criarmos um gráfico que mostra a mudança de valor de um veículo em determinado período selecionado pelo usuário. Apenas carros apareceram para seleção nesse projeto, mas a Api Fipe retorna valores para caminhões e motocicletas.

## Objetivo
O objetivo principal do Go Fipe é permitir que os usuários verifiquem a variação de preço do seu veículo de forma fácil.
---
## Funcionalidades
O Go Fipe oferece as seguintes funcionalidades:

1. Consulta de Preços: O usuário pode pesquisar o seu veículo de forma simples e completa, selecionando o ano, modelo do carro e selecionando o período que queira verificar sua variação de preço.
2. Visualização simplificada: No programa é fácil de visualizar o valor do veículo no período em um gráfico criado dinamicamente.
---
## Como utilizar esse projeto
Para rodar esse projeto na sua máquina é preciso:
- Instalar python 3.12 ou mais recente.
- Criar um ambiente django server. Nome do projeto: goFipe / Crie também um app chamado: core.
- Instalar a biblioteca requests no ambiente.
- Utilize o ambiente para executar os arquivos esse projeto.
## Estrutura de pastas e arquivos do projeto
#### Pasta Map:
1. Mapeamento-chamadas.py - O arquivo com exemplos de chamadas em python para a api da tabela fipe, seguimos de exemplo as chamadas do projeto [precodeveiculo](https://github.com/giovanigenerali/precodeveiculo) de [@giovanigenerali](https://github.com/giovanigenerali).
   
#### Pasta do APP Core. Nela esta os arquivos principais do projeto:
1. Models.py - Classes e Métodos do backend, como chamadas e tratamento de dados passados para as views.
2. Views.py – Aqui se encontra as funções para apresentar os dados do backend para o fron-end via o forms.
3. Form.py - Formulário que é utilizado no front-end para o usuário selecionar o veículo. As opções de seleção são informadas dinamicamente pelas views.
4. Tests.py - Aqui se encontra os testes unitários do projeto.
   
#### Pasta templates, na raiz do projeto:
1. Index.html - Front-end principal do projeto, acessando o formulário e o gráfico por variáveis no projeto Django.
2. Grafico.html - Arquivo com o front-end do gráfico do projeto, utilizamos a biblioteca chart.js para esse projeto com o plugin ChartDataLabels para alteração da apresentação do valor no formulário para Real brasileiro.
3. Restante dos arquivos - São utilizados complementado as views para apresentar o as opções dos formulários toda vez que a opções anterior por selecionada.

---
### Integrantes do Grupo
+ Henrique Souza
+ Lucas Braich
+ Luiz Felipe Aguiar
+ Welison Pereira
+ Isadora Santos

##### UniBH - 2024
