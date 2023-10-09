from interface.Tela_Deletar import Tela_Deletar
from interface.Tela_Consulta import Tela_Consulta
from interface.Tela_Alterar import Tela_Alterar

import PySimpleGUI as sg

matriz = [
    ['jsdbfj', 557, 'dm', 4174],
    ['asjfa', 456, 'abc', 4574],
    ['mjkg', 5343, 'vv', 7896],
    ['jbawr', 43, 'vix', 645]
]

janela = Tela_Alterar(matriz, 1)

while True:
    evento, valor = janela.read()

    if evento == sg.WIN_CLOSED:
        janela.close()
        break

