def Tela_Alterar(matriz):
    import PySimpleGUI as sg
    from interface.Detalhes import detalhes

    
    sg.theme(detalhes['tema'])
    
    tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz)]
  
    tamanho_matriz = []
    for id in range(len(matriz)):
        tamanho_matriz.append(id)
  
    lista_colunas = [
        'Motorista', 
        'Linha', 
        'destino', 
        'Passsageiro'
    ]
  

    tabela_teste = [[sg.Table(values = tabela_comId, headings=['ID','MOTORISTA', 'LINHA', 'DESTINO', 'N° DE PASSAGEIROS'], justification='left', key='tabela', enable_click_events=True)]]

    frame_teste = [
        [sg.Frame('Informações',  [
            [sg.Text('Informe a linha:  ', background_color= detalhes['corFundo'], text_color= detalhes['corTexto']), sg.InputCombo(values=tamanho_matriz, size=(10, 1), key='ID_linha')],
            
            [sg.Text('Informe a coluna:', background_color= detalhes['corFundo'], text_color= detalhes['corTexto']), sg.InputCombo(values=lista_colunas, size=(10, 1), key='ID_coluna')],

            [sg.Text('  ', background_color= detalhes['corFundo'])],
            
            [sg.Text('Novo Dado:', background_color= detalhes['corFundo'], text_color= detalhes['corTexto']), sg.Input(key='NOVO_DADO', size=(10, 1))],
            [sg.Button('Voltar', size= detalhes['sizeBotao']), sg.Button('Confirmar', size= detalhes['sizeBotao'])]
        ], background_color= detalhes['corFundo'], element_justification='c', title_location='n')]
    ]
  
    layout_alterar = [
        [sg.Menu([
            ['Menu', ['Menu Principal', 'Sair']],
            ['Navegar', ['Inserir', 'Ver Tudo', 'Consulta Específica', 'Deletar']],
            ['Ajuda', ['Conta', 'Sobre...']]
        ], 
            key='barra_menu', background_color= detalhes['corFundo'], text_color= detalhes['corTexto'])
        ],
        [sg.Column(tabela_teste, element_justification='c', background_color= detalhes['corFundo']), sg.VSep(), sg.Column(frame_teste, element_justification='c', background_color= detalhes['corFundo'])],
    ]
  
    return sg.Window('ALTERAR',layout_alterar, background_color=  detalhes['corFundo'], element_justification= 'c', finalize= True)
