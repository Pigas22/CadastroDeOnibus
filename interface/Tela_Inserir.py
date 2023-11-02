def Tela_Inserir():
    import PySimpleGUI as sg
    from interface.Detalhes import detalhes

    
    sg.theme(detalhes['tema'])
    
    layout_inserir = [
        [sg.Menu([
            ['Menu', ['Menu Principal', 'Sair']], 
            ['Navegar', ['Consulta Específica', 'Ver Tudo', 'Alterar', 'Deletar']], 
            ['Ajuda', ['Conta', 'Sobre...']]
            ], key= 'barra_menu', background_color= detalhes['corFundo'], text_color= detalhes['corTexto'])],
        [sg.Text('MOTORISTA:', size = (15, 1), background_color=detalhes['corFundo']), sg.Input(key='motorista', background_color='White', text_color= 'Black')],
        [sg.Text('LINHA ÔNIBUS:', size=(15,1), background_color=detalhes['corFundo']), sg.Input(key='linha', background_color='White', text_color= 'Black')],
        [sg.Text('DESTINO:', size=(15, 1), background_color=detalhes['corFundo']), sg.Input(key='destino',background_color='white', text_color= 'Black')],
        [sg.Text('N° de PASSAGEIROS:', size=(15, 1), background_color=detalhes['corFundo']), sg.Input(key='N° de PASSAGEIROS', background_color='white', text_color= 'Black')],
        [sg.Button('Voltar', size= detalhes['sizeBotao']), sg.Button('Cadastrar', size= detalhes['sizeBotao'])]
    ]
  
    return sg.Window('INSERIR', layout_inserir, background_color= detalhes['corFundo'], finalize= True)
