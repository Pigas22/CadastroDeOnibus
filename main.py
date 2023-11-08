import PySimpleGUI as sg
from backend import Colunas_Inversa
from backend.Funcoes.Matriz import Matriz
from backend.Funcoes.Usuario import Usuario
from interface.Tela_Cadastro import Tela_Cadastro
from interface.Tela_Login import Tela_Login
from interface.Tela_Inicial import Tela_Inicial
from interface.Tela_Inserir import Tela_Inserir
from interface.Tela_VerTudo import Tela_VerTudo
from interface.Tela_Deletar import Tela_Deletar
from interface.Tela_Consulta import Tela_Consulta 
from interface.Tela_Alterar import Tela_Alterar
from interface.Popup_Creditos import Popup_Creditos
from interface.PopupCreditosImagens import PopupCreditosImagens
from interface.Popup_Padrao import Popup_Padrao
from interface.Popup_Save import Popup_Save
from interface.Tela_PerfilUser import Tela_PerfilUser
from interface.Op_MenuBAR import op_menuBar
from interface.Detalhes import detalhes


# Janelas
janelaCadastro = Tela_Cadastro()
janelaLogin = None
janelaInicial = None
janelaInserir = None
janelaVerTudo = None
janelaDeletar = None
janelaConsulta = None
janelaAlterar = None
janelaPerfilUser = None

# Parametro para salvar automaticamente as alterações
auto_Save = False

# Parametro para mostrar as Senhas na tela de Login, Cadastro e Perfil
mostrarLogin = False
mostrarCadastro = False
mostrarSenha = False

# Tipo e filtro de dado da Tela alterar, padrao == ID
tipo = 'ID'
filtro = 'id'

# Classes
user = Usuario()
matriz = Matriz()

# Leitura de janelas e seus valores e eventos
while True:
    window, evento, valor = sg.read_all_windows()
    matriz.setContadorAlteracao()

    if window == janelaCadastro:
        validacoes = 0
        
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            janelaCadastro.close()
            PopupCreditosImagens()
            exit()

        if evento == 'Cadastrar Dados' or evento == 'KP_Enter:104' or evento == 'Return:36':
            user.setNomeUser(valor['Nome_Completo'])
            user.setEmailUser(valor['Email'])
            user.setSenha1User(valor['Senha_Principal'])
            user.setSenha2User(valor['Senha_Confirmação'])
            
            user.verificarSenha()
            user.verificarEmail()
            
            email_Valido = user.getEmailVerificado()
            senha_Valida = user.getSenhaVerificada()

            if (senha_Valida and email_Valido) and (user.getSenha1User() != '' and user.getSenha2User() != '' and user.getEmailUser() != ''):
                validacoes += 2

            elif not email_Valido and user.getEmailUser() != '':
                Popup_Padrao('Email já cadastrado anteriormente!', 'O email informado já está vinculado a uma conta, por favor, informe outro endereço de email ou logue na conta.')    
            
            elif user.getEmailUser() == '':
                Popup_Padrao('Email não informado!', 'Por favor, informe um email para continuar.')
      
            elif not senha_Valida and user.getSenha1User() != '':
                Popup_Padrao('Senha incorreta!', 'As senhas informadas não coincidem ou A senha está fraca. \n| As senhas devem conter números e caracteres especiais, como: ! @ # ( : *.')   
            
            elif user.getSenha1User() == '' or user.getSenha2User() == '':
                Popup_Padrao('Senha não informada!', 'Por favor, informe uma senha para continuar.')
                

            if validacoes == 2:
                with open('backend/BD_Contas/Todas_Contas.txt', 'r') as arquivo:
                    linhas = len(arquivo.readlines())
                arquivo.close()

                user.setIdUser(linhas + 1)
                Id_User = user.getIdUser()
                matriz.setIdUserMatriz(Id_User)
                
                
                try:
                    salvo = user.salvarConta()
                    Popup_Padrao(f'{salvo}', 'Parabéns, agora você pode utilizar o programa com sua conta e ter seus dados salvos.')

                except Exception as error:
                    Popup_Padrao('ERROR!!', 'Aconteceu algum erro ao salvar sua conta, tente novamente.')

                else:
                    arquivo = open(f'backend/BD_Dados/Usuario{Id_User}_Dados.txt', 'xt') # criando arquivo
                    arquivo.close()
        
                    janelaCadastro.close()
                    
                    matriz.Inicializar()
                    janelaInicial = Tela_Inicial()


        elif evento == 'Limpar':
            lacunas = [janelaCadastro['Nome_Completo'], janelaCadastro['Email'], janelaCadastro['Senha_Principal'], janelaCadastro['Senha_Confirmação']]
            for lacuna in lacunas:
                lacuna.update('')

        elif evento == '__VerSenha__' and mostrarCadastro:
            mostrarCadastro = False

            janelaCadastro['__VerSenha__'].update(image_filename= r'interface/olho aberto.png', image_subsample= 20)
            janelaCadastro['Senha_Principal'].update(password_char= '*')
            janelaCadastro['Senha_Confirmação'].update(password_char= '*')
    
        elif evento == '__VerSenha__' and not mostrarCadastro:
            mostrarCadastro = True
    
            janelaCadastro['__VerSenha__'].update(image_filename= r'interface/olho fechado.png', image_subsample= 20)
            janelaCadastro['Senha_Principal'].update(password_char= '')
            janelaCadastro['Senha_Confirmação'].update(password_char= '')

    
    elif window == janelaLogin:
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            janelaLogin.close()
            PopupCreditosImagens()
            exit()

        elif evento == 'Fazer Login' or evento == 'KP_Enter:104' or evento == 'Return:36':
            validacao = 0

            user.setLoginEmailUser(valor['Email_Login'])
            user.setLoginSenhaUser(valor['Senha_Login'])
      
            if user.getLoginEmailUser() != "" and user.getLoginSenhaUser() != "":
                user.verificarEmail()
                user.verificarSenha()

                email_Existente = user.getEmailVerificado()
                senha_Valida = user.getSenhaVerificada()
    
                if email_Existente and senha_Valida:
                    user.setIdUser(login= True)
                    Id_User = user.getIdUser()
                    matriz.setIdUserMatriz(Id_User= Id_User)
                    validacao += 2    
    
                elif not email_Existente:
                    Popup_Padrao('Email incorreto!', 'O email informado não à nenhuma conta vinculado.')
    
                elif not senha_Valida:
                    Popup_Padrao('Senha Incorreta!', 'Por favor, digite-a novamente.')
    
                if validacao == 2:
                    Popup_Padrao('Login Efetuado com Sucesso!', 'Aproveite o App.')
                    janelaLogin.close()
                    
                    matriz.Inicializar()
                    janelaInicial = Tela_Inicial()
              
            else:
                Popup_Padrao('Email e senha não informados!', 'Por favor, informe-os para efetuar o login.')

        
        elif evento == 'VerSenha' and mostrarLogin:
            mostrarLogin = False

            janelaLogin['VerSenha'].update(image_filename= r'interface/olho aberto.png', image_subsample= 20)
            janelaLogin['Senha_Login'].update(password_char= '*')
        
        
        elif evento == 'VerSenha' and not mostrarLogin:
            mostrarLogin = True
    
            janelaLogin['VerSenha'].update(image_filename= r'interface/olho fechado.png', image_subsample= 20)
            janelaLogin['Senha_Login'].update(password_char= '')
        
    
    elif window == janelaInicial:
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            salvar = Popup_Save()
            if salvar == 'Yes':
                matriz.Salvar_Matriz()
                matriz.Inicializar()

            janelaInicial.close()
            PopupCreditosImagens()
            exit()


    elif window == janelaInserir:
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            salvar = Popup_Save()
            if salvar == 'Yes':
                matriz.Salvar_Matriz()
                matriz.Inicializar()

            janelaInserir.close()
            PopupCreditosImagens()
            exit()
      
        elif evento == 'Cadastrar':
            motorista = valor['motorista']    
            linha = valor['linha']
            destino = valor['destino']
            quant_passageiros = valor['N° de PASSAGEIROS']
    
            matriz.Inserir(motorista, linha, destino, quant_passageiros)
            Popup_Padrao('Viagem adicionada com sucesso!', 'Confira a nova adição na tela "Ver Tudo".')

            lacunas = [janelaInserir['motorista'], janelaInserir['linha'], janelaInserir['destino'], janelaInserir['N° de PASSAGEIROS']]
            for lacuna in lacunas:
                lacuna.update('')


    elif window == janelaVerTudo:
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            janelaVerTudo.close()
            PopupCreditosImagens()
            exit()
        

    elif window == janelaDeletar:
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            salvar = Popup_Save()
            if salvar == 'Yes':
                matriz.Salvar_Matriz()
                matriz.Inicializar()

            janelaDeletar.close()
            PopupCreditosImagens()
            exit()

        elif evento[0] == 'tabela_atual':
            selected_id = janelaDeletar['ID']
            selected_id.update(evento[2][0])
            valor['ID'] = evento[2][0]

        elif evento == 'Deletar Dado' or evento == 'Resetar Matriz':
            try:
                if evento == 'Deletar Dado':
                    id_do_registro = int(valor['ID'])
            
                    matriz.Deletar(local_linha= id_do_registro)

                elif evento == 'Resetar Matriz':
                    matriz.Deletar(resetar= True)

                tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz.getMatriz())]
                
                tabela = janelaDeletar['tabela_atual']
                tabela.update(values=tabela_comId)
                
                Popup_Padrao('Operação bem-sucedida', 'Valor deletado com sucesso!')
                resp_delete = janelaDeletar['ID']
                resp_delete.update('')

            except ValueError:
                Popup_Padrao('ERROR!', 'Nenhum ID informado.')

    
    elif window == janelaConsulta:
        filtros_Keys = ['FILTRO_ID', 'FILTRO_MOTORISTA', 'FILTRO_LINHA', 'FILTRO_DESTINO', 'FILTRO_PESSOAS']
    
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            janelaConsulta.close()
            PopupCreditosImagens()
            exit()

        elif evento == 'CONFIRMAR':
            janelaConsulta['MATRIZ_ORIGINAL'].update(False)
            try:
                chave_pesquisa = valor['KEY_PESQUISA']
                if valor['FILTRO_MOTORISTA'] or valor['FILTRO_DESTINO']:
                    chave_pesquisa = chave_pesquisa.title()
                    
                else:
                    chave_pesquisa = int(chave_pesquisa)
    
                matriz_Pesquisa = []
                
                if filtro == 'id':
                    matriz_Pesquisa.append(matriz.getMatriz()[int(chave_pesquisa)])

                else:
                    for linha in matriz.getMatriz():
                        if filtro == 0 or filtro == 2: # Motorista e Destino
                            if type(linha[filtro]) == type(chave_pesquisa):
                                if linha[filtro] == chave_pesquisa:
                                    matriz_Pesquisa.append(linha)

                            else:
                                # provocando erro
                                int('abc')

                        elif filtro == 1 or filtro == 3: # Linha e Quantidade de Pessoas
                            if int(linha[filtro]) == int(chave_pesquisa):
                                matriz_Pesquisa.append(linha)

                    if len(matriz_Pesquisa) == 0:
                        # provocando o erro
                        print(matriz_Pesquisa[99])

                matriz.LogMatriz(f'Operação realizada com sucesso! Dado Consultado: [ {chave_pesquisa} ] do tipo [ {tipo} ]')

                tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz_Pesquisa)]
                janelaConsulta['tabela'].update(values=tabela_comId)

                janelaConsulta['KEY_PESQUISA'].update('')
                
            except IndexError:
                Popup_Padrao('Error: ', 'Não possui esse dado no Banco de Dados')
                matriz.LogMatriz(f'ERROR: Não possui esse dado no Banco de Dados \nDado consultado: [ {chave_pesquisa} ] do tipo [ {tipo} ]')

            except ValueError:
                Popup_Padrao('Error:', 'Dado informado não coincide com o filtro selecionado.')
                matriz.LogMatriz(f'ERROR: Dado informado não coincide com o filtro selecionado. \nDado consultado: [ {chave_pesquisa} ] do tipo [ {tipo} ]')

        elif evento in filtros_Keys:
            if valor['FILTRO_ID']:
                filtro = 'id'
                tipo = 'ID'
                
            elif valor['FILTRO_MOTORISTA']:
                filtro = 0
                tipo = 'Motorista'
    
            elif valor['FILTRO_LINHA']: 
                filtro = 1
                tipo = 'Linha'
                
            elif valor['FILTRO_DESTINO']: 
                filtro = 2
                tipo = 'Destino'
    
            elif valor['FILTRO_PESSOAS']: 
                filtro = 3
                tipo = 'Quantidade de pessoas'

        elif evento == 'MATRIZ_ORIGINAL':
            tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz.getMatriz())]
            tabela = janelaConsulta['tabela']
            tabela.update(values=tabela_comId)

    
    elif window == janelaAlterar:
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            salvar = Popup_Save()
            if salvar == 'Yes':
                matriz.Salvar_Matriz()
                matriz.Inicializar()

            janelaAlterar.close()
            PopupCreditosImagens()
            exit()

        elif evento[0] == 'tabela':
            tabela = janelaAlterar['ID_linha']
            tabela.update(evento[2][0])

            tabela2 = janelaAlterar['ID_coluna']
            tabela2.update(Colunas_Inversa.colunas_inversa[str(evento[2][1])])

            valor['ID_linha'] = evento[2][0]
            valor['ID_coluna'] = Colunas_Inversa.colunas_inversa[str(evento[2][1])]
      
        elif evento == 'Confirmar':
            try:
                ID_linha = valor['ID_linha']
                ID_coluna = valor['ID_coluna']
                new_dado = valor['NOVO_DADO']

                if ID_coluna == 'Linha' or ID_coluna == 'Passageiro':
                    new_dado = int(valor['NOVO_DADO'])

                else:
                    if new_dado.isnumeric():
                        int('abc')

                    else:
                        new_dado = new_dado.title()

                matriz.Alterar_Dado(ID_linha, ID_coluna, new_dado)
        
                tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz.getMatriz())]
                tabela = janelaAlterar['tabela']
                tabela.update(values=tabela_comId)
        
                Popup_Padrao('Operação bem-sucedida', 'Valor alterado com sucesso!')
                resposta = janelaAlterar['NOVO_DADO']
                resposta.update('')

            except ValueError:
                Popup_Padrao('Error:', 'Dado informado não coincide com a coluna selecionada.')
                matriz.LogMatriz(f'ERROR: Dado informado não coincide com a coluna selecionada. \n    - Dado consultado: [ {new_dado} ] \n    - Coluna selecionada: [ {ID_coluna} ]')


    elif window == janelaPerfilUser:   
        if evento == '__ATIVAR__':
            auto_Save = True
            janelaPerfilUser['__ESTADO__'].update('ON ', text_color='green')

        elif evento == '__DESATIVAR__':
            auto_Save = False
            janelaPerfilUser['__ESTADO__'].update('OFF', text_color='red')
        

        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            janelaPerfilUser.close()
            PopupCreditosImagens()
            exit()


        elif evento == '__EditarNome__':
            novo_nome = sg.popup_get_text('Informe o novo Nome do Usuário: ', background_color= detalhes['corFundo'])

            if novo_nome != None:
                user.setNomeUser(novo_nome)
                janelaPerfilUser['__NOME__'].update(novo_nome)
                user.salvarConta(atualizar_nome= True)

                Popup_Padrao('Parabéns dado alterado com sucesso!', 'O Nome da conta foi alterada com sucesso.')

            else:
                Popup_Padrao('Error: Nenhum dado informado', 'Por favor, insira algum nome válido.')


        elif evento == '__EditarEmail__':
            novo_email = sg.popup_get_text('Informe o novo Email do Usuário: ', background_color= detalhes['corFundo'])
            if novo_email != None:
                user.verificarEmail(atualizar_dado= True, novo_email= novo_email)

                email_Valido = user.getEmailVerificado()
                if email_Valido:
                    user.setEmailUser(novo_email)
                    janelaPerfilUser['__EMAIL__'].update(novo_email)
                    user.salvarConta(atualizar_email= True)

                    Popup_Padrao('Parabéns dado alterado com sucesso!', 'O Email da conta foi alterada com sucesso.')

                else:
                    Popup_Padrao('Error: Email informado já existe', 'Por favor, insira outro email.')
            
            else:
                Popup_Padrao('Error: Nenhum dado informado', 'Por favor, insira algum email válido.')
            

        elif evento == '__EditarSenha__':
            nova_senha = sg.popup_get_text('Informe a nova Senha do Usuário: ', background_color= detalhes['corFundo'], password_char= '*')
            if nova_senha != None:
                user.verificarSenha(atualizar_dado= True, nova_senha= nova_senha)

                senha_Valida = user.getSenhaVerificada()
                print(senha_Valida)
                if senha_Valida:
                    user.setSenha1User(nova_senha)

                    if mostrarSenha:
                        user.setSenhaDesencripatada()
                        senha_secreta = user.getSenhaDesencriptada()

                    elif not mostrarSenha:
                        senha_secreta = len(nova_senha) * '*'
                    
                    janelaPerfilUser['__SENHA__'].update(senha_secreta)
                    user.salvarConta(atualizar_senha= True)

                    Popup_Padrao('Parabéns dado alterado com sucesso!', 'A Senha da conta foi alterada com sucesso.')

                else:
                    Popup_Padrao('Error: Senha informada é Inválida', 'Por favor, insira alguma senha válida.')
                
            else:
                Popup_Padrao('Error: Nenhum dado informado', 'Por favor, insira alguma senha válida.')


        elif evento == '__VerSenha__':
            user.setSenhaDesencripatada()
            senha_Desencriptada = user.getSenhaDesencriptada()
            
            if mostrarSenha:
                mostrarSenha = False
                janelaPerfilUser['__VerSenha__'].update(image_filename= r'interface/olho aberto.png', image_subsample= 20)
                janelaPerfilUser['__SENHA__'].update(len(senha_Desencriptada) * '*')    
            
            elif not mostrarSenha:
                mostrarSenha = True
                janelaPerfilUser['__VerSenha__'].update(image_filename= r'interface/olho fechado.png', image_subsample= 20)
                janelaPerfilUser['__SENHA__'].update(senha_Desencriptada)


        elif evento == 'Logout':
            user.__init__()

                  
    if evento in op_menuBar:
        if evento not in ['Sair', 'Sobre...', 'Salvar']:
            window.close()
        
        if evento in ['Menu Principal', 'Voltar', 'VoltarMenu']:
            if auto_Save and evento != 'VoltarMenu':
                matriz.Salvar_Matriz()
                matriz.Inicializar()

            janelaInicial = Tela_Inicial()

        elif evento in ['Cadastro', 'VoltarCadastro', 'Logout']:
            janelaCadastro = Tela_Cadastro()

        elif evento in ['Login', 'Login...']:
            janelaLogin = Tela_Login()

        elif evento in ['Conta', '__Conta__']:
            janelaPerfilUser = Tela_PerfilUser(Id_User, auto_Save)

        elif evento in ['Inserir', 'INSERIR']:
            janelaInserir = Tela_Inserir()
        
        elif evento in ['Ver Tudo', 'VER TUDO']:
            janelaVerTudo = Tela_VerTudo(matriz.getMatriz(), Id_User)

        elif evento in ['Deletar', 'DELETAR']:
            janelaDeletar = Tela_Deletar(matriz.getMatriz())

        elif evento in ['Consulta Específica', 'CONSULTA ESPECÍFICA']:
            janelaConsulta = Tela_Consulta(matriz.getMatriz())
            
        elif evento in ['Alterar', 'ALTERAR']:
            janelaAlterar = Tela_Alterar(matriz.getMatriz())

        elif evento == 'Sobre...':
            Popup_Creditos()

        elif evento == 'Salvar':
            matriz.Salvar_Matriz()
            matriz.Inicializar()
