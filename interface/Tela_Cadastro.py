def Tela_Cadastro(): 
    import PySimpleGUI as sg
    from interface.Detalhes import detalhes
    
    sg.theme(detalhes['tema'])
  
    col1 = [
        [sg.Text('| Nome Completo: *', background_color= detalhes['corFundo'])],
        [sg.Input(key='Nome_Completo', size=(25, 1))]
    ]

    col2 = [
        [sg.Text('| Informe seu Email: *', background_color=detalhes['corFundo'])],
        [sg.Input(key='Email', size=(25, 1))]
    ]

    col3 = [
        [sg.Text('| Digite sua senha: *', background_color=detalhes['corFundo'])],
        [sg.Input(key='Senha_Principal', size=(25, 1), password_char='*')]
    ]

    col4 = [
        [sg.Text('| Confirme sua senha: *', background_color=detalhes['corFundo'])],
        [sg.Input(key='Senha_Confirmação', size=(25, 1), password_char='*')]
    ]

    Barra_Menu = [
        ['Menu', ['Login', 'Sair']], 
        ['Ajuda', ['Sobre...']]
    ]
  
    layout = [
        [sg.Menu(Barra_Menu)],
        [sg.Image(r'interface/ImageUser.png', background_color='Slate Blue')],
        [sg.Column(col1, background_color=detalhes['corFundo']), sg.Column(col2, background_color=detalhes['corFundo'])],
        [sg.Column(col3, background_color=detalhes['corFundo']), sg.Column(col4, background_color=detalhes['corFundo'])],
        [sg.Frame('Obs: ', [[sg.Text('As senhas devem conter números e caracteres especiais, \ncomo: ! @ # $ %', background_color=detalhes['corFundo'])]], background_color=detalhes['corFundo'])],
        [sg.Button('Limpar', size= detalhes['sizeBotão']), sg.Button('Login...', size= detalhes['sizeBotão']), sg.Button('Cadastrar Dados', size= detalhes['sizeBotão'])]
    ]

    return sg.Window('Cadastro', layout, background_color= detalhes['corFundo'], element_justification= 'c', size = (500, 400), return_keyboard_events= True, finalize= True)
