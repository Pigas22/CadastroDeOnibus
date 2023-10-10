def Tela_VerTudo(matriz, Id_User):
    import PySimpleGUI as sg
    from interface.Detalhes import detalhes


    sg.theme(detalhes['tema'])

    col1 = [
        [sg.Button('Voltar', size= detalhes['sizeBotão'])]
    ]
    
    layout_verTudo = [
        [sg.Menu([['Menu', ['Menu Principal', 'Sair']], ['Navegar', ['Inserir', 'Consulta Específica', 'Alterar', 'Deletar']], ['Ajuda', ['Sobre...']]], 
                 key='barra_menu', 
                 background_color=  detalhes['corFundo'], 
                 text_color= detalhes['corTexto'])
        ],
        [sg.Table(values = matriz, headings=[ 'MOTORISTA', 'LINHA', 'DESTINO', 'N° DE PASSAGEIROS'], justification='left', expand_y= True)],
        [sg.Column(col1, element_justification= 'left', background_color= detalhes['corFundo'])]
    ]

    return sg.Window('VER TUDO', layout_verTudo, background_color= detalhes['corFundo'], finalize= True, size= (500, 350))
