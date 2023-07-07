import PySimpleGUI as sg
import backend

# layout 1 == botoes
sg.theme('DarkBlue')
op_menuBar = ['Menu', 'Menu Principal', 'Sair', 'Navegar', 'Inserir', 'Ver Tudo', 'Consulta Específica', 'Deletar', 'Ajuda', 'Sobre...']
op_menuPrincpal = ['INSERIR', 'DELETAR', 'ALTERAR', 'VER TUDO', 'CONSULTA ESPECÍFICA']

def tela_inicial():
  sair = ''
  matriz = backend.inicializar()
    
  layout = [
    [sg.Menu([['Menu', ['Menu Principal', 'Sair']], ['Ajuda', ['Sobre...']]],
            key='barra_menu', 
            background_color='SlateBlue', 
            text_color='Black')
            ],
    [sg.Text('OPERADOR DE TABELAS', font='Arial 20 bold', background_color='White', text_color='Black')],
    [sg.Text('', background_color='SlateBlue')],
    [sg.Button('INSERIR', size=(24, 2)), sg.Button('ALTERAR', size=(24, 2))],
    [sg.Button('DELETAR', size=(24, 2)), sg.Button('VER TUDO', size=(24, 2))],
    [sg.Button('CONSULTA ESPECÍFICA', size=(50, 2))]       
  ]  
  
  tela_inicial = sg.Window('Operador de Tabelas', layout, background_color='SlateBlue', element_justification='c', size = (500, 250))
  
  while True:  
    evento, valor = tela_inicial.read()
    if evento == sg.WINDOW_CLOSED or sair == 'Sair':
      break
    
    elif evento in op_menuPrincpal:
      tela_inicial.close()
      if evento == 'INSERIR':
        sair = tela_inserir(matriz)

      elif evento == 'VER TUDO':
        sair = tela_verTudo(matriz)
    
      elif evento == 'DELETAR':
        sair = tela_deletar(matriz)
    
      elif evento == 'CONSULTA ESPECÍFICA':
        sair = tela_consulta(matriz)
      
      elif evento == 'ALTERAR':
        sair = tela_alterar(matriz)

    elif evento in op_menuBar:
      if evento == 'Menu Principal':
        tela_inicial()

      elif evento == 'Sair':
        sair = 'Sair'

      elif evento == 'Sobre...':
        print('Feito por: \nSamuel Paiva Paizante \nThiago Holz Coutinho \nVínicius Rocha Aleixo')

    backend.salvar(matriz)
    tela_inicial()
    
  tela_inicial.close()  
  

def tela_verTudo(matriz):
  layout_verTudo = [
    [sg.Menu([['Menu', ['Menu Principal', 'Sair']], ['Navegar', ['Inserir', 'Consulta Específica', 'Alterar', 'Deletar']], ['Ajuda', ['Sobre...']]],
          key='barra_menu', 
          background_color='SlateBlue', 
          text_color='Black')
          ],
    [sg.Table(values = matriz, headings=[ 'MOTORISTA', 'LINHA', 'DESTINO', 'PASSAGEIROS'], justification='left')]
  ]

  tela_verTudo = sg.Window('VER TUDO' , layout_verTudo, background_color='SlateBlue')
  
  while True:
    evento, valor = tela_verTudo.read()
    if evento == sg.WINDOW_CLOSED:
      break

    if evento in op_menuBar:
      tela_verTudo.close()
      if evento == 'Menu Principal':
        tela_inicial()

      elif evento == 'Sair':
        return 'Sair'

      elif evento == 'Inserir':
        tela_inserir(matriz)

      elif evento == 'Alterar':
        tela_alterar(matriz)

      elif evento == 'Consulta Específica':
        tela_consulta(matriz)

      elif evento == 'Deletar':
        tela_deletar(matriz)

      elif evento == 'Sobre...':
        print('Feito por: \nSamuel Paiva Paizante \nThiago Holz Coutinho \nVínicius Rocha Aleixo')


def tela_inserir(matriz):
  layout_inserir = [
    [sg.Menu([['Menu', ['Menu Principal', 'Sair']], ['Navegar', ['Consulta Específica', 'Ver Tudo', 'Alterar', 'Deletar']], ['Ajuda', ['Sobre...']]],
              key='barra_menu', 
              background_color='SlateBlue', 
              text_color='Black')
              ],
    [sg.Text('MOTORISTA:', size = (11, 1), background_color='SlateBlue'), sg.Input(key='motorista', background_color='White', text_color='Black')],
    [sg.Text('LINHA ÔNI:', size=(11,1), background_color='SlateBlue'), sg.Input(key='linha', background_color='White', text_color='Black')],
    [sg.Text('DESTINO:', size=(11, 1), background_color='SlateBlue'), sg.Input(key='destino',background_color='white', text_color='black')],
    [sg.Text('PASSAGEIROS:', size=(11, 1), background_color='SlateBlue'), sg.Input(key='PASSAGEIROS', background_color='white', text_color='Black')],
    [sg.Button('Cadastrar')]
  ]
  
  tela_inserir = sg.Window('INSERIR' , layout_inserir, background_color='SlateBlue')
  
  while True:
    evento, valor = tela_inserir.read()
    if evento == sg.WINDOW_CLOSED:
      break
      
    elif evento == 'Cadastrar':
      motorista = valor['motorista']    
      linha = valor['linha']
      destino = valor['destino']
      passageiros = valor['PASSAGEIROS']

      backend.inserir(matriz, motorista, linha, destino, passageiros)

      tela_inserir.close()

    elif evento in op_menuBar:
      tela_inserir.close()
      if evento == 'Menu Principal':
        tela_inicial()

      elif evento == 'Sair':
        return 'Sair'

      elif evento == 'Alterar':
        tela_alterar(matriz)

      elif evento == 'Ver Tudo':
        tela_verTudo(matriz)

      elif evento == 'Consult Específica':
        tela_consulta(matriz)

      elif evento == 'Deletar':
        tela_deletar(matriz)

      elif evento == 'Sobre...':
        print('Feito por: \nSamuel Paiva Paizante \nThiago Holz Coutinho \nVínicius Rocha Aleixo')


def tela_deletar(matriz):
  tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz)]
  layout_deletar = [
    [sg.Menu([['Menu', ['Menu Principal', 'Sair']], ['Navegar', ['Inserir', 'Ver Tudo', 'Consulta Específica', 'Alterar']], ['Ajuda', ['Sobre...']]],
              key='barra_menu', 
              background_color='SlateBlue', 
              text_color='Black')
              ],
    [sg.Table(values = tabela_comId , headings=['ID','MOTORISTA', 'LINHA', 'DESTINO', 'PASSAGEIROS'], justification='left', key='tabela_atual')],
    [sg.Text('DIGITE O ID DO REGISTRO QUE DESEJA DELETAR:',  background_color='SlateBlue', text_color='Black')],
    [sg.Input(key='ID', size=(10,1)), sg.Button('CONFIRMAR')]
  ]

  tela_deletar = sg.Window('DELETAR' , layout_deletar, background_color='SlateBlue', element_justification='c')
  
  while True:
    evento, valor = tela_deletar.read()
    if evento == sg.WINDOW_CLOSED:
      tela_deletar.close()
      break
    
    elif evento in op_menuBar:
      tela_deletar.close()
      if evento == 'Menu Principal':
        tela_inicial()

      elif evento == 'Sair':
        return 'Sair'

      elif evento == 'Inserir':
        tela_inserir(matriz)

      elif evento == 'Ver Tudo':
        tela_verTudo(matriz)

      elif evento == 'Consulta Específica':
        tela_consulta(matriz)

      elif evento == 'Alterar':
        tela_alterar(matriz)

      elif evento == 'Sobre...':
        print('Feito por: \nSamuel Paiva Paizante \nThiago Holz Coutinho \nVínicius Rocha Aleixo')

    elif evento == 'CONFIRMAR':
      id_do_registro = int(valor['ID'])

      backend.deletar(matriz, local_linha=id_do_registro)
      tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz)]

      tabela = tela_deletar['tabela_atual']
      tabela.update(values=tabela_comId)


def tela_consulta(matriz):
   tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz)]
  
   layout_consulta = [
     [sg.Menu([['Menu', ['Menu Principal', 'Sair']], ['Navegar', ['Inserir', 'Ver Tudo', 'Alterar', 'Deletar']], ['Ajuda', ['Sobre...']]],
              key='barra_menu', 
              background_color='SlateBlue', 
              text_color='Black')
              ],
    [sg.Text('DIGITE O ID DO REGISTRO QUE DESEJA CONSULTAR:',  background_color='SlateBlue', text_color='Black')],
    [sg.Input(key='ID', size=(10, 1)), sg.Button('CONFIRMAR')],
   [sg.Table(values = tabela_comId, headings=['ID','MOTORISTA', 'LINHA', 'DESTINO', 'PASSAGEIRO'], justification='left')]
   ]
  
   tela_consulta = sg.Window('CONSULTA ESPECÍFICA', layout_consulta, background_color='SlateBlue', element_justification='c')
   while True:
    evento, valor = tela_consulta.read()
    if evento == sg.WINDOW_CLOSED:
      break

    elif evento in op_menuBar:
      tela_consulta.close()
      if evento == 'Menu Principal':
        tela_inicial()

      elif evento == 'Sair':
        return 'Sair'

      elif evento == 'Inserir':
        tela_inserir(matriz)

      elif evento == 'Ver Tudo':
        tela_verTudo(matriz)

      elif evento == 'Alterar':
        tela_alterar(matriz)

      elif evento == 'Deletar':
        tela_deletar(matriz)

      elif evento == 'Sobre...':
        print('Feito por: \nSamuel Paiva Paizante \nThiago Holz Coutinho \nVínicius Rocha Aleixo')

    elif evento == 'CONFIRMAR':
      ID = valor['ID']
      print(ID)


def tela_alterar(matriz):
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
    [sg.Text('Informe a linha:', background_color='SlateBlue', text_color='Black')],
    [sg.InputCombo(values=tamanho_matriz, size=(9, 1), key='ID_linha')]
  ]

  col2 = [
    [sg.Text('Informe a coluna:', background_color='SlateBlue', text_color='Black')],
    [sg.InputCombo(values=lista_colunas, size=(9, 1), key='ID_coluna')]
  ]
  

  tabela_teste = [[sg.Table(values = tabela_comId, headings=['ID','MOTORISTA', 'LINHA', 'DESTINO', 'PASSAGEIRO'], justification='left', key='tabela', enable_click_events=True)]]

  frame_teste = [[sg.Frame('Informações',  [
    [sg.Column(col1, element_justification='c', background_color='SlateBlue'), sg.VSep(), sg.Column(col2, element_justification='c', background_color='SlateBlue')],
    [sg.Text('  ', background_color='SlateBlue')],
    [sg.Text('Novo Dado:', background_color='SlateBlue', text_color='Black'), sg.Input(key='NOVO_DADO', size=(10, 1))],
    [sg.Button('CONFIRMAR')]
  ], background_color='SlateBlue', element_justification='c', title_location='n')]]

  
  layout_alterar = [
    [sg.Menu([['Menu', ['Menu Principal', 'Sair']], ['Navegar', ['Inserir', 'Ver Tudo', 'Consulta Específica', 'Deletar']], ['Ajuda', ['Sobre...']]],
              key='barra_menu', 
              background_color='SlateBlue', 
              text_color='Black')
              ],
    [sg.Column(tabela_teste, element_justification='c', background_color='SlateBlue'), sg.VSep(), sg.Column(frame_teste, element_justification='c', background_color='SlateBlue')],
  ]
  
  tela_alterar = sg.Window('ALTERAR',layout_alterar, background_color='SlateBlue', element_justification='c')
  
  while True:
    evento, valor = tela_alterar.read()
    if evento == sg.WINDOW_CLOSED:
      break
    
    elif evento in op_menuBar:
      tela_alterar.close()
      if evento == 'Menu Principal':
        tela_inicial()

      elif evento == 'Sair':
        return 'Sair'

      elif evento == 'Inserir':
        tela_inserir(matriz)

      elif evento == 'Ver Tudo':
        tela_verTudo(matriz)

      elif evento == 'Consulta Específica':
        tela_consulta(matriz)

      elif evento == 'Deletar':
        tela_deletar(matriz)

      elif evento == 'Sobre...':
        print('Feito por: \nSamuel Paiva Paizante \nThiago Holz Coutinho \nVínicius Rocha Aleixo')
      
    elif evento[0] == 'tabela':
      tabela = tela_alterar['ID_linha']
      tabela.update(evento[2][0])

      tabela2 = tela_alterar['ID_coluna']
      tabela2.update(backend.colunas_inversa[str(evento[2][1])])

      valor['ID_linha'] = evento[2][0]
      valor['ID_coluna'] = backend.colunas_inversa[str(evento[2][1])]
      
    elif evento == 'CONFIRMAR':
      ID_linha = valor['ID_linha']
      ID_coluna = valor['ID_coluna']
      new_dado = valor['NOVO_DADO']
      
      backend.alterar_dado(matriz, ID_linha, ID_coluna, new_dado)
      backend.salvar(matriz)
      
      tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz)]
      tabela = tela_alterar['tabela']
      tabela.update(values=tabela_comId)
