def Tela_Inicial(Id_User):
    import PySimpleGUI as sg
    from main import detalhes
    

    sg.theme(detalhes['tema'])
    
    layout = [
        [sg.Menu([['Menu', ['Menu Principal', 'Sair']], ['Ajuda', ['Perfil', 'Sobre...']]], key='barra_menu', background_color= detalhes['corFundo'], text_color='Black')],
        [sg.Text('OPERADOR DE TABELAS', font=f'{detalhes["fonte"]} 20 bold', background_color='White', text_color= detalhes['corTexto'])],
        [sg.Text('', background_color= detalhes['corFundo'])],
        [sg.Button('INSERIR', size=(24, 2)), sg.Button('ALTERAR', size=(24, 2))],
        [sg.Button('DELETAR', size=(24, 2)), sg.Button('VER TUDO', size=(24, 2))],
        [sg.Button('CONSULTA ESPECÍFICA', size=(50, 2))]       
    ]  
  
    return sg.Window('Operador de Tabelas', layout, background_color= detalhes['corFundo'], element_justification= 'c', size= (500, 250), finalize= True)
