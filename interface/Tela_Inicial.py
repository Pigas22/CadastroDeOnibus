import PySimpleGUI as sg


def Tela_Inicial():
    from interface.Detalhes import detalhes
    

    sg.theme(detalhes['tema'])

    col1 = [
        [sg.Text('', background_color= detalhes['corFundo']), sg.Button(button_color= detalhes['corFundo'], border_width= 0, image_subsample= 4, image_filename= r'interface\ImageUser.png', key= '__Conta__')],
    ]
    
    col2 = [
        [sg.Text('              ', background_color= detalhes['corFundo']), sg.Text('OPERADOR DE TABELAS', font=f'{detalhes["fonte"]} 20 bold', background_color='White', text_color= 'Black')],
    ]


    layout = [
        [sg.Menu([
            ['Menu', ['Menu Principal', 'Salvar', 'Sair']], 
            ['Ajuda', ['Conta', 'Sobre...']]
            ], key='barra_menu', background_color= detalhes['corFundo'], text_color='Black')],
        [sg.Column(col2, background_color= detalhes['corFundo'], element_justification= 'r'), sg.Column(col1, background_color= detalhes['corFundo'], element_justification= 'r')],
        [sg.Text('', background_color= detalhes['corFundo'])],
        [sg.Button('INSERIR', size=(24, 2)), sg.Button('ALTERAR', size=(24, 2))],
        [sg.Button('DELETAR', size=(24, 2)), sg.Button('VER TUDO', size=(24, 2))],
        [sg.Button('CONSULTA ESPECÍFICA', size=(50, 2))]       
    ]  
  
    return sg.Window('Operador de Tabelas', layout, background_color= detalhes['corFundo'], element_justification= 'c', size= (527, 250), finalize= True)
