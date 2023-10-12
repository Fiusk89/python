import PySimpleGUI as sg
from atm import atm

layout = [
    [sg.Text('Bem vindo ao ATM do Fiusk!')],
    [sg.Text('Quanto você quer sacar?')],
    [sg.InputText(key='saque')],
    [sg.Button('Sacar'), sg.Button('Cancelar')],
    [sg.Text('', key='texto_saque')]
]

janela = sg.Window('ATM do Fiusk', layout)

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    if event == 'Sacar':
        saque = values['saque']
        sq = atm(saque)
        janela['texto_saque'].Update(f'Você sacou R${saque}.')

janela.close()