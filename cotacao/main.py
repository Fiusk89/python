import PySimpleGUI as sg
from cotacao import pegar_cotacoes

layout = [
    [sg.Text('Pegar Cotação da Moeda')],
    [sg.InputText(key='nome_cotacao')],
    [sg.Button('Rodar'), sg.Button('Cancelar')],
    [sg.Text('', key='texto_cotacao')],
]

janela = sg.Window('Sistema de Cotaçôes', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    if evento == 'Rodar':
        codigo_cotacao = valores['nome_cotacao']
        cotacao = pegar_cotacoes(codigo_cotacao)
        janela['texto_cotacao'].Update(f'A cotação do {codigo_cotacao} é de R${cotacao}')



janela.close()