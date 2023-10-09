def Tela_Consulta(matriz, Id_User): # Ainda à modificar
    import PySimpleGUI as sg
    from interface.Detalhes import detalhes
    

    sg.theme(detalhes['tema'])

    tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz)]

    layout_Frame = [
        [
            sg.Radio('ID', "__FILTRO__", background_color= detalhes['corFundo'], default=True, key='FILTRO_ID', enable_events=True), 
            sg.Radio('MOTORISTA', "__FILTRO__", background_color= detalhes['corFundo'], key='FILTRO_MOTORISTA', enable_events=True), 
            sg.Radio('LINHA', "__FILTRO__", background_color= detalhes['corFundo'], key='FILTRO_LINHA', enable_events=True)],
        [
            sg.Radio('DESTINO', "__FILTRO__", background_color= detalhes['corFundo'], key='FILTRO_DESTINO', enable_events=True), 
            sg.Radio('N° DE PESSOAS', "__FILTRO__", background_color= detalhes['corFundo'], key='FILTRO_PESSOAS', enable_events=True)
        ]
    ]

    layout_ColunaEsq = [
        [
            sg.Table(values = tabela_comId, headings=['ID','MOTORISTA', 'LINHA', 'DESTINO', 'N° DE PESSOAS'], justification='left', key='tabela')
        ],
        [
            sg.Button('Voltar', size= detalhes['sizeBotão']),
            sg.Checkbox('Mostrar tabela sem filtro', background_color= detalhes['corFundo'], text_color='White', font= detalhes['fonte'], enable_events=True, key='MATRIZ_ORIGINAL')
        ]
    ]

    layout_ColunaDir = [
        [sg.Text('| Selecione o Filtro da pesquisa:', background_color= detalhes["corFundo"], font=f'{detalhes["fonte"]} {detalhes["tamanhoFonte"]}', text_color= detalhes['corTexto'])],
        [sg.Frame('Filtro', layout=layout_Frame, background_color= detalhes['corFundo'])],

        [sg.Text('', background_color= detalhes['corFundo'])],
        
        [sg.Text('| Informe o Dado Abaixo:',  background_color= detalhes['corFundo'], font=f'{detalhes["fonte"]} {detalhes["tamanhoFonte"]}', text_color= detalhes['corTexto'])],
        [sg.Input(key='KEY_PESQUISA', size=(20, 1)), sg.Button('CONFIRMAR', size= detalhes['sizeBotão'])]
    ]
  
    layout_consulta = [
        [sg.Menu([
            ['Menu', ['Menu Principal', 'Sair']],
            ['Navegar', ['Inserir', 'Ver Tudo', 'Alterar', 'Deletar']],
            ['Ajuda', ['Sobre...']]
        ], key='barra_menu', background_color= detalhes['corFundo'], text_color='Black')],   
        [
            sg.Column(layout_ColunaEsq, background_color= detalhes['corFundo'], element_justification='center'),
            sg.VSep(), 
            sg.Column(layout_ColunaDir, background_color= detalhes['corFundo'], element_justification='left')
        ]
    ]
  
    return sg.Window('CONSULTA ESPECÍFICA', layout_consulta, background_color= detalhes['corFundo'], element_justification= 'c', finalize= True)
