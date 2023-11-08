def Tela_Deletar(matriz): # à modificar
    import PySimpleGUI as sg
    from interface.Detalhes import detalhes
    

    sg.theme(detalhes['tema'])
    
    tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz)]

    col1_tabela = [
        [sg.Table(values = tabela_comId , headings=['ID','MOTORISTA', 'LINHA', 'DESTINO', 'N° DE PASSAGEIROS'], justification='left', key='tabela_atual', enable_click_events=True)]
    ]

    col_Botao = [
        [sg.Button('Resetar Matriz', size= (12, 1)), sg.Button('Deletar Dado', size= detalhes['sizeBotao'])]
    ]

    layoutFrame = [
        [sg.Text("*Apenas ID's são válidos.", background_color= detalhes['corFundo'])]
    ]

    col2 = [
        [sg.Text(' ', background_color= detalhes['corFundo'])],
        [sg.Text('| Informe o ID que deseja excluir:',  background_color= detalhes['corFundo'], text_color= detalhes['corTexto'], font= f'{detalhes["fonte"]} {detalhes["tamanhoFonte"]}')], 
        [sg.Input(key='ID', size=(30, 1))],
        [sg.Frame('Obs.:', layoutFrame, background_color= detalhes['corFundo'])],
        [sg.Text(' ', background_color= detalhes['corFundo'])],
        [sg.Column(col_Botao, background_color= detalhes['corFundo'], justification= 'right')]
    ]

    col3 = [
        [sg.Button('Voltar', size= detalhes['sizeBotao'])]
    ]

    layout_deletar = [
        [sg.Menu([
            ['Menu', ['Menu Principal', 'Salvar', 'Sair']],
            ['Navegar', ['Inserir', 'Ver Tudo', 'Consulta Específica', 'Alterar']],
            ['Ajuda', ['Conta', 'Sobre...']]
        ], key='barra_menu', background_color= detalhes['corFundo'], text_color= detalhes['corTexto'])],
        [sg.Column(col1_tabela, background_color= detalhes['corFundo']), sg.Column(col2, background_color= detalhes['corFundo'])],
        [sg.Column(col3, background_color= detalhes['corFundo'], justification= 'left')],
    ]
    
    return sg.Window('DELETAR' , layout_deletar, background_color=  detalhes['corFundo'], element_justification= 'c', finalize= True)
