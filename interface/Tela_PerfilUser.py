def Tela_PerfilUser(Id_User, auto_Save): # a ser feito
    import PySimpleGUI as sg
    from interface.Detalhes import detalhes

    
    sg.theme(detalhes['tema'])

    with open(r'backend\BD_Contas\Todas_Contas.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    arquivo.close()

    for conta in linhas:
        contas = conta.split()

        if int(contas[0]) == int(Id_User):
            break

    senha = int(len(contas[3]) / 2) * '*'

    if auto_Save:
        text_estado = sg.Text(text='ON ', text_color= 'green', background_color= detalhes['corFundo'], key= '__ESTADO__')

    else:
        text_estado = sg.Text(text='OFF', text_color= 'red', background_color= detalhes['corFundo'], key= '__ESTADO__')


    col1 = [
        [sg.Text('| Nome: ', background_color= detalhes['corFundo'])],
        [sg.Text('     ', background_color= detalhes['corFundo']), sg.Text(f'{contas[1]}', background_color= detalhes['corFundo'], text_color= 'Black', font= 'Arial 14 underline', key= '__NOME__')],
        [sg.Text('| Email: ', background_color= detalhes['corFundo'])],
        [sg.Text('     ', background_color= detalhes['corFundo']), sg.Text(f'{contas[2]}', background_color= detalhes['corFundo'], text_color= 'Black', font= 'Arial 14 underline', key= '__EMAIL__')],
        [sg.Text('| Senha: ', background_color= detalhes['corFundo'])],
        [sg.Button(button_color= detalhes['corFundo'], border_width= 0, image_subsample= 24, image_filename= r'interface\olho aberto.png', key= '__VerSenha__'), sg.Text(f'{senha}', background_color= detalhes['corFundo'], text_color= 'Black', font= 'Arial 14 underline', key= '__SENHA__')],
        [sg.Text('| Salvar Automaticamente: ', background_color= detalhes['corFundo']), text_estado], 
        [sg.Radio('Ativar', '__AUTOSAVE__', key= '__ATIVAR__', background_color= detalhes['corFundo'], enable_events= True, default= (auto_Save)), sg.Radio('Desativar', '__AUTOSAVE__', key= '__DESATIVAR__', background_color= detalhes['corFundo'], enable_events= True, default= (not auto_Save))],
    ]

    col2 = [
        [sg.Text('', background_color= detalhes['corFundo'])],
        [sg.Button(button_color= detalhes['corFundo'], border_width= 0, image_subsample= 24, image_filename= r'interface\lapis.png', key= '__EditarNome__')],
        [sg.Text('', background_color= detalhes['corFundo'])],
        [sg.Button(button_color= detalhes['corFundo'], border_width= 0, image_subsample= 24, image_filename= r'interface\lapis.png', key= '__EditarEmail__')],
        [sg.Text('', background_color= detalhes['corFundo'])],
        [sg.Button(button_color= detalhes['corFundo'], border_width= 0, image_subsample= 24, image_filename= r'interface\lapis.png', key= '__EditarSenha__')],
        [sg.Text('', background_color= detalhes['corFundo'])],
        [sg.Text('', background_color= detalhes['corFundo'])],
    ]


    layout_Frame = [
        [sg.Column(col1, background_color= detalhes['corFundo']), sg.Text('      ', background_color= detalhes['corFundo']), sg.Column(col2, background_color= detalhes['corFundo'])],
        [sg.Button('Voltar', key= 'VoltarMenu', size= detalhes['sizeBotao']), sg.Text('                                ', background_color= detalhes['corFundo']), sg.Button('Logout', size= detalhes['sizeBotao'])],
    ]

    layout_PerfilUser = [
        [sg.Menu([
            ['Menu', ['Menu Principal', 'Sair']],
            ['Navegar', ['Inserir', 'Ver Tudo', 'Consulta Específica', 'Alterar']],
            ['Ajuda', ['Sobre...']]
        ], key='barra_menu', background_color= detalhes['corFundo'], text_color= detalhes['corTexto'])],
        [sg.Image(r'interface\ImageUser.png', background_color= detalhes['corFundo'])],
        [sg.Frame('Informações da conta: ', layout_Frame, background_color= detalhes['corFundo'])]
    ]
    

    return sg.Window('Perfil', layout= layout_PerfilUser, background_color= detalhes['corFundo'], element_justification= 'c', size= (370, 460), finalize= True)