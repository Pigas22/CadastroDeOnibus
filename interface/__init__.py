import PySimpleGUI as sg
import backend


sg.theme('DarkBlue')
op_menuBar = ['Menu', 'Menu Principal', 'Sair', 'Navegar', 'Inserir', 'Ver Tudo', 'Consulta Específica', 'Deletar', 'Ajuda', 'Sobre...']
op_menuPrincpal = ['INSERIR', 'DELETAR', 'ALTERAR', 'VER TUDO', 'CONSULTA ESPECÍFICA']


def tela_cadastro():   
  validacoes = 0
  sair = ''
  
  col1 = [
    [sg.Text('| Nome Completo: *', background_color='SlateBlue')],
    [sg.Input(key='Nome_Completo', size=(25, 1))],
    [sg.Text('| Digite sua senha: *', background_color='SlateBlue')],
    [sg.Input(key='Senha_Principal', size=(25, 1), password_char='*')]
  ]

  col2 = [
    [sg.Text('| Informe seu Email: *', background_color='SlateBlue')],
    [sg.Input(key='Email', size=(25, 1))],
    [sg.Text('| Confirme sua senha: *', background_color='SlateBlue')],
    [sg.Input(key='Senha_Confirmação', size=(25, 1), password_char='*')]
  ]
  
  
  layout = [
    [sg.Menu([['Menu', ['Login', 'Sair']], ['Ajuda', ['Sobre...']]])],
    [sg.Text('Login...', size=(40, 1), justification='r', background_color='Slate Blue', enable_events=True, font='Arial 15 underline')],
    [sg.Image(r'ImageUser.png', background_color='Slate Blue')],
    [sg.Column(col1, background_color='SlateBlue'), sg.Column(col2, background_color='SlateBlue')],
    [sg.Frame('Obs: ', [[sg.Text('Todos os campos com Asterisco (*) devem ser preenchidos.', background_color='SlateBlue')]], background_color='SlateBlue')],
    [sg.Button('Limpar Dados'), sg.Button('Salvar')]
  ]

  tela_cadastro = sg.Window('Cadastro', layout, background_color='SlateBlue', element_justification='c', size = (520, 410))

  while True:
    evento, valor = tela_cadastro.read()
    
    if evento == sg.WINDOW_CLOSED or sair == 'Sair':
      break

    if evento == 'Login' or evento == 'Login...':
      tela_cadastro.close()
      tela_login()

    if evento == 'Sair':
      sair = 'Sair'

    if evento == 'Salvar':
      nome_Completo = valor['Nome_Completo'] 
      email = valor['Email']
      senha_Principal = valor['Senha_Principal']
      senha_Confirmacao = valor['Senha_Confirmação']

      email_valido = backend.verificar_email(email)
      senha_valida = backend.verificar_senha(senha_Principal, senha_Confirmacao)

      if senha_valida and email_valido: 
        # varifica a senha e o email se estao devidamente corretos
        validacoes += 2

      elif not email_valido:
        sg.popup('Email já cadastrado anteriormente!', 'O email informado já está vinculado a uma conta, por favor, informe outro endereço de email ou logue na conta.', background_color='Slate Blue')
      
      elif not senha_valida:
        sg.popup('Senha incorreta!', 'As senhas informadas não coincidem ou A senha está fraca. \n| As senhas devem conter números e caracteres especiais, como: ! @ # ( : *.', background_color='Slate Blue')

      if validacoes == 2:
        backend.salvar_contas(nome_Completo, email, senha_Principal)
        with open('backend/BD_Contaas', 'r') as arquivo:
          linhas = len(arquivo.readlines())
        arquivo.close()

        with open(f'backend/BD_Dados/Usuario{linhas+1}_Dados.txt', 'xt') as arquivo:
          arquivo.close()
        
        
        sg.popup('Conta criada com sucesso!!', 'Parabéns, agora você pode utilizar o programa com sua conta e ter seus dados salvos.', background_color=  'SlateBlue')
        
        tela_cadastro.close()
        tela_inicial()

    if evento == 'Limpar Dados':
      lacunas = [tela_cadastro['Nome_Completo'], tela_cadastro['Email'], tela_cadastro['Senha_Principal'], tela_cadastro['Senha_Confirmação']]
      for lacuna in lacunas:
        lacuna.update('')


def tela_login():
  # Não terminado 
  layout = [
    [sg.Image(r'ImageUser.png', background_color='Slate Blue')],
    [sg.Text('| Email:                               ', background_color='Slate Blue')],
    [sg.Input(key='Email_Login', size=(20, 1))],
    [sg.Text('| Senha:                               ', background_color='Slate Blue')],
    [sg.Input(key='Senha_Login', size=(20, 1), password_char='*')],
    [sg.Button('Limpar Dados'), sg.Button('Entrar')]
  ]

  tela_login = sg.Window('Login', layout, background_color='Slate Blue', element_justification='c', size=(300, 330))

  while True:
    evento, valor = tela_login.read()

    if evento == sg.WINDOW_CLOSED:
      break

    elif evento == 'Entrar':
      validacao = 0

      email_Login = valor['Email_Login']
      senha_Login = valor['Senha_Login']
      
      if email_Login and senha_Login:
        email_Valido = backend.verificar_email(email_Login)
        if email_Valido:
          sg.popup('Email incorreto!', 'O email informado não está vinculado à nenhuma conta')

        else:
          validacao += 1

        senha_Valida = backend.verificar_senha(senha_Login, email_Login=email_Login)
        if senha_Valida:
          validacao += 1

        else:
          sg.popup('Senha Incorreta!', 'Por favor, digite-a novamente.')
          

        if validacao == 2:
          sg.popup('Login Efetuado com Sucesso!', 'Aproveite o App.')
          tela_inicial()

      else:
        sg.popup('Email e senha não informados!', 'Por favor, informe-os para efetuar o login.')


    elif evento == 'Limpar Dados':
      lacunas = [tela_login['Email_Login'], tela_login['Senha_Login']]
      for lacuna in lacunas:
        lacuna.update('')


def tela_inicial():
  sair = ''
  matriz = backend.inicializar()
    
  layout = [
    [sg.Menu([['Menu', ['Menu Principal', 'Sair']], ['Ajuda', ['Perfil', 'Sobre...']]],
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
    [sg.Table(values = matriz, headings=[ 'MOTORISTA', 'LINHA', 'DESTINO', 'N° DE PASSAGEIROS'], justification='left')]
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
    [sg.Text('MOTORISTA:', size = (15, 1), background_color='SlateBlue'), sg.Input(key='motorista', background_color='White', text_color='Black')],
    [sg.Text('LINHA ÔNIBUS:', size=(15,1), background_color='SlateBlue'), sg.Input(key='linha', background_color='White', text_color='Black')],
    [sg.Text('DESTINO:', size=(15, 1), background_color='SlateBlue'), sg.Input(key='destino',background_color='white', text_color='black')],
    [sg.Text('N° de PASSAGEIROS:', size=(15, 1), background_color='SlateBlue'), sg.Input(key='N° de PASSAGEIROS', background_color='white', text_color='Black')],
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
      quant_passageiros = valor['N° de PASSAGEIROS']

      backend.inserir(matriz, motorista, linha, destino, quant_passageiros)

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
    [sg.Table(values = tabela_comId , headings=['ID','MOTORISTA', 'LINHA', 'DESTINO', 'N° DE PASSAGEIROS'], justification='left', key='tabela_atual', enable_click_events=True)],
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

    elif evento[0] == 'tabela_atual':
      selected_id = tela_deletar['ID']
      selected_id.update(evento[2][0])
      valor['ID'] = evento[2][0]

    elif evento == 'CONFIRMAR':
      id_do_registro = int(valor['ID'])

      backend.deletar(matriz, local_linha=id_do_registro)
      tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz)]

      tabela = tela_deletar['tabela_atual']
      tabela.update(values=tabela_comId)

      sg.popup_auto_close('Operação bem-sucedida', 'Valor deletado com sucesso! ', background_color='SlateBlue', text_color='Black', font='Arial 12')
      resp_delete = tela_deletar['ID']
      resp_delete.update('')


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
   [sg.Table(values = tabela_comId, headings=['ID','MOTORISTA', 'LINHA', 'DESTINO', 'N° DE PASSAGEIROS'], justification='left')]
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
    [sg.InputCombo(values=tamanho_matriz, size=(10, 1), key='ID_linha')]
  ]

  col2 = [
    [sg.Text('Informe a coluna:', background_color='SlateBlue', text_color='Black')],
    [sg.InputCombo(values=lista_colunas, size=(10, 1), key='ID_coluna')]
  ]
  

  tabela_teste = [[sg.Table(values = tabela_comId, headings=['ID','MOTORISTA', 'LINHA', 'DESTINO', 'N° DE PASSAGEIROS'], justification='left', key='tabela', enable_click_events=True)]]

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
        sg.popup('Feito por:', 'Samuel Paiva Paizante \nThiago Holz Coutinho \nVínicius Rocha Aleixo')
      
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
      
      sg.popup_auto_close('Operação bem-sucedida', 'Valor alterado com sucesso! ', background_color='SlateBlue', text_color='Black', font='Arial 12')
      resposta = tela_alterar['NOVO_DADO']
      resposta.update('')


def tela_creditos():
  print()