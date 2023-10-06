def Tela_Alterar(matriz, Id_User):
    import PySimpleGUI as sg
    from main import detalhes

    
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

    col1 = [
        [sg.Text('Informe a linha:', background_color= detalhes['corFundo'], text_color= detalhes['corTexto'])],
        [sg.InputCombo(values=tamanho_matriz, size=(10, 1), key='ID_linha')]
    ]

    col2 = [
        [sg.Text('Informe a coluna:', background_color= detalhes['corFundo'], text_color= detalhes['corTexto'])],
        [sg.InputCombo(values=lista_colunas, size=(10, 1), key='ID_coluna')]
    ]
  

    tabela_teste = [[sg.Table(values = tabela_comId, headings=['ID','MOTORISTA', 'LINHA', 'DESTINO', 'N° DE PASSAGEIROS'], justification='left', key='tabela', enable_click_events=True)]]

    frame_teste = [
        [sg.Frame('Informações',  [
            [sg.Column(col1, element_justification='c', background_color= detalhes['corFundo']), sg.VSep(), sg.Column(col2, element_justification='c', background_color= detalhes['corFundo'])],
            [sg.Text('  ', background_color= detalhes['corFundo'])],
            [sg.Text('Novo Dado:', background_color= detalhes['corFundo'], text_color= detalhes['corTexto']), sg.Input(key='NOVO_DADO', size=(10, 1))],
            [sg.Button('CONFIRMAR')]
        ], background_color= detalhes['corFundo'], element_justification='c', title_location='n')]
    ]
  
    layout_alterar = [
        [sg.Menu([
            ['Menu', ['Menu Principal', 'Sair']],
            ['Navegar', ['Inserir', 'Ver Tudo', 'Consulta Específica', 'Deletar']],
            ['Ajuda', ['Sobre...']]
        ], 
            key='barra_menu', background_color= detalhes['corFundo'], text_color= detalhes['corTexto'])
        ],
        [sg.Column(tabela_teste, element_justification='c', background_color= detalhes['corFundo']), sg.VSep(), sg.Column(frame_teste, element_justification='c', background_color= detalhes['corFundo'])],
    ]
  
    return sg.Window('ALTERAR',layout_alterar, background_color=  detalhes['corFundo'], element_justification= 'c', finalize= True)
