def Tela_Deletar(matriz, Id_User): # à modificar
    import PySimpleGUI as sg
    from main import detalhes
    

    sg.theme(detalhes['tema'])
    
    tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz)]
    layout_deletar = [
        [sg.Menu([['Menu', ['Menu Principal', 'Sair']], ['Navegar', ['Inserir', 'Ver Tudo', 'Consulta Específica', 'Alterar']], ['Ajuda', ['Sobre...']]], 
                 key='barra_menu', 
                 background_color= detalhes['corFundo'], 
                 text_color= detalhes['corTexto'])
        ],
        [sg.Table(values = tabela_comId , headings=['ID','MOTORISTA', 'LINHA', 'DESTINO', 'N° DE PASSAGEIROS'], justification='left', key='tabela_atual', enable_click_events=True)],
        [sg.Text('DIGITE O ID DO REGISTRO QUE DESEJA DELETAR:',  background_color= detalhes['corFundo'], text_color= detalhes['corTexto'])],
        [sg.Input(key='ID', size=(10,1)), sg.Button('CONFIRMAR')]
    ]

    return sg.Window('DELETAR' , layout_deletar, background_color=  detalhes['corFundo'], element_justification= 'c', finalize= True)
