def Tela_Login(): # Não terminado
    import PySimpleGUI as sg
    from interface.Detalhes import detalhes

    
    sg.theme(detalhes['tema'])
    
    Barra_Menu = [
        ['Menu', ['Cadastro', 'Sair']], 
        ['Ajuda', ['Sobre...']]
    ]
    
    layout = [
        [sg.Menu(Barra_Menu)],
        [sg.Image(r'interface/ImageUser.png', background_color= detalhes['corFundo'])],
        [sg.Text('| Email:                                          ', background_color= detalhes['corFundo'])],
        [sg.Input(key='Email_Login', size=(20, 1)), sg.Text('      ', background_color= detalhes['corFundo'])],
        [sg.Text('| Senha:                                          ', background_color= detalhes['corFundo'])],
        [sg.Input(key='Senha_Login', size=(20, 1), password_char='*'), sg.Button(button_color= detalhes['corFundo'], border_width= 0, image_subsample= 20, image_filename= r'interface/olho aberto.png', key= 'VerSenha')],
        [sg.Text('', background_color= detalhes['corFundo'])],
        [sg.Button('Voltar', size= detalhes['sizeBotao'], key='VoltarCadastro'), sg.Button('Fazer Login', size= detalhes['sizeBotao'])],
    ]

    return sg.Window('Login', layout, background_color= detalhes['corFundo'], element_justification= 'c', size= (295, 345), return_keyboard_events= True, finalize= True)
