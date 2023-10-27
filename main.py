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
from interface.Popup_Padrao import Popup_Padrao
from interface.Tela_PerfilUser import Tela_PerfilUser # Vou usar ainda
from interface.Op_MenuBAR import op_menuBar


janelaCadastro = Tela_Cadastro()
janelaLogin = None
janelaInicial = None
janelaInserir = None
janelaVerTudo = None
janelaDeletar = None
janelaConsulta = None
janelaAlterar = None
janelaPerfilUser = None
popupCreditos = None
popupPadrao = None

user = Usuario()
matriz = Matriz()

while True:
    window, evento, valor = sg.read_all_windows()

    if window == janelaCadastro:
        validacoes = 0
        
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            janelaCadastro.close()
            exit()

        elif evento == 'Cadastrar Dados' or evento == 'KP_Enter:104' or evento == 'Return:36':
            user.setNomeUser(valor['Nome_Completo'])
            user.setEmailUser(valor['Email'])
            user.setSenha1User(valor['Senha_Principal'])
            user.setSenha2User(valor['Senha_Confirmação'])
            
            user.verificarSenha()
            user.verificarEmail()
            
            email_valido = user.getEmailVerificado()
            senha_valida = user.getSenhaVerificada()
            

            if (senha_valida and email_valido) and (user.getSenha1User() != '' and user.getSenha2User() != '' and user.getEmailUser() != ''): 
                # varifica a senha e o email se estao devidamente corretos
                validacoes += 2

            elif not email_valido and user.getEmailUser() != '':
                Popup_Padrao('Email já cadastrado anteriormente!', 'O email informado já está vinculado a uma conta, por favor, informe outro endereço de email ou logue na conta.')    
            elif user.getEmailUser() == '':
                Popup_Padrao('Email não informado!', 'Por favor, informe um email para continuar.')
      
            elif not senha_valida and user.getSenha1User() != '':
                Popup_Padrao('Senha incorreta!', 'As senhas informadas não coincidem ou A senha está fraca. \n| As senhas devem conter números e caracteres especiais, como: ! @ # ( : *.')   
            elif user.getSenha1User() == '' or user.getSenha2User() == '':
                Popup_Padrao('Senha não informada!', 'Por favor, informe uma senha para continuar.')
                

            if validacoes == 2:
                with open('backend/BD_Contas/Todas_Contas.txt', 'r') as arquivo:
                    linhas = len(arquivo.readlines())
                arquivo.close()

                user.setIdUser(linhas + 1 )
                Id_User = user.getIdUser()
                matriz.setIdUserMatriz()
                
                try:
                    salvo = user.salvarConta()

                except Exception:
                    Popup_Padrao('ERROR!!', 'Aconteceu algum erro ao salvar sua conta, tente novamente.')
                    

                else:
                    with open(f'backend/BD_Dados/Usuario{Id_User}_Dados.txt', 'xt') as arquivo:
                        arquivo.close()
    
                    Popup_Padrao(f'{salvo}', 'Parabéns, agora você pode utilizar o programa com sua conta e ter seus dados salvos.')
        
                    janelaCadastro.close()
                    
                    matriz.Inicializar()
                    janelaInicial = Tela_Inicial(Id_User)


                

            elif evento == 'Limpar':
                lacunas = [janelaCadastro['Nome_Completo'], janelaCadastro['Email'], janelaCadastro['Senha_Principal'], janelaCadastro['Senha_Confirmação']]
                for lacuna in lacunas:
                    lacuna.update('')

    
    elif window == janelaLogin:
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            janelaLogin.close()
            exit()

        elif evento == 'Fazer Login' or evento == 'KP_Enter:104' or evento == 'Return:36':
            validacao = 0

            user.setLoginEmailUser(valor['Email_Login'])
            user.setLoginSenhaUser(valor['Senha_Login'])
      
            if user.getLoginEmailUser() != "" and user.getLoginSenhaUser() != "":
                user.verificarEmail()
                email_Existe = not user.getEmailVerificado() # Se o email existir retorna False, caso contrário, True
    
                if email_Existe:
                    Id_User = user.getIdUser()
                    matriz.setIdUserMatriz()
                    validacao += 1    
    
                else:
                    Popup_Padrao('Email incorreto!', 'O email informado não está vinculado à nenhuma conta')
                    
                user.verificarSenha()
                senha_Valida = user.getSenhaVerificada()
                if senha_Valida:
                    validacao += 1
    
                else:
                    Popup_Padrao('Senha Incorreta!', 'Por favor, digite-a novamente.')
              
    
                if validacao == 2:
                    Popup_Padrao('Login Efetuado com Sucesso!', 'Aproveite o App.')
                    janelaLogin.close()
                    
                    matriz.Inicializar()
                    janelaInicial = Tela_Inicial(Id_User)
              
    
            else:
                Popup_Padrao('Email e senha não informados!', 'Por favor, informe-os para efetuar o login.')

        elif evento == 'LimparEmail':
            janelaLogin['Email_Login'].update('')

        elif evento == 'LimparSenha':
            janelaLogin['Senha_Login'].update('')

    
    elif window == janelaInicial:
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            janelaInicial.close()
            exit()


    elif window == janelaInserir:
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
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
            exit()
            

    elif window == janelaDeletar:
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            janelaDeletar.close()
            exit()

        elif evento[0] == 'tabela_atual':
            selected_id = janelaDeletar['ID']
            selected_id.update(evento[2][0])
            valor['ID'] = evento[2][0]

        elif evento == 'Confirmar' or evento == 'Resetar Matriz':
            if evento == 'Confirmar':
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
    
    
    elif window == janelaConsulta:
        filtro = 'id'
        filtros_Keys = ['FILTRO_ID', 'FILTRO_MOTORISTA', 'FILTRO_LINHA', 'FILTRO_DESTINO', 'FILTRO_PESSOAS']
    
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            janelaConsulta.close()
            exit()

        elif evento == 'CONFIRMAR':
            janelaConsulta['MATRIZ_ORIGINAL'].update(False)
            try:
                chave_pesquisa = valor['KEY_PESQUISA']
                if valor['FILTRO_MOTORISTA'] or valor['FILTRO_DESTINO']:
                    chave_pesquisa = chave_pesquisa.title()
                    
                matriz_Pesquisa = []
    
                if chave_pesquisa.isnumeric():
                    chave_pesquisa = int(chave_pesquisa)
                
                if filtro == 'id':
                    try:
                        matriz_Pesquisa.append(matriz.getMatriz()[int(chave_pesquisa)])

                    except ValueError:
                        Popup_Padrao('Error:', 'Informe apenas o ID do Ônibus')
    
                else:
                    for linha in matriz.getMatriz():
                        if linha[filtro] == chave_pesquisa:
                            matriz_Pesquisa.append(linha)

                    if len(matriz_Pesquisa) == 0:
                        Popup_Padrao('Error: ', 'Não possui esse dado no Banco')
    
                tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz_Pesquisa)]
                janelaConsulta['tabela'].update(values=tabela_comId)

                janelaConsulta['KEY_PESQUISA'].update('')


            except IndexError:
                Popup_Padrao('Error: ', 'Não possui esse dado no Banco')
        
        elif evento in filtros_Keys:
            if valor['FILTRO_ID']:
                filtro = 'id'
                
            elif valor['FILTRO_MOTORISTA']:
                filtro = 0
    
            elif valor['FILTRO_LINHA']: 
                filtro = 1
                
            elif valor['FILTRO_DESTINO']: 
                filtro = 2
    
            elif valor['FILTRO_PESSOAS']: 
                filtro = 3

        elif evento == 'MATRIZ_ORIGINAL':
            tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz.getMatriz())]
            tabela = janelaConsulta['tabela']
            tabela.update(values=tabela_comId)

    
    elif window == janelaAlterar:
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            janelaAlterar.close()
            janelaInicial = Tela_Inicial(Id_User)

      
        elif evento[0] == 'tabela':
            tabela = janelaAlterar['ID_linha']
            tabela.update(evento[2][0])

            tabela2 = janelaAlterar['ID_coluna']
            tabela2.update(Colunas_Inversa.colunas_inversa[str(evento[2][1])])

            valor['ID_linha'] = evento[2][0]
            valor['ID_coluna'] = Colunas_Inversa.colunas_inversa[str(evento[2][1])]
      
        elif evento == 'Confirmar':
            ID_linha = valor['ID_linha']
            ID_coluna = valor['ID_coluna']
            new_dado = valor['NOVO_DADO']
      
            matriz.Alterar_Dado(ID_linha, ID_coluna, new_dado)
            matriz.Salvar_Matriz()
      
            tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz.getMatriz())]
            tabela = janelaAlterar['tabela']
            tabela.update(values=tabela_comId)
      
            Popup_Padrao('Operação bem-sucedida', 'Valor alterado com sucesso!')
            resposta = janelaAlterar['NOVO_DADO']
            resposta.update('')

    
    if evento in op_menuBar:
        if evento != 'Sair':
            window.close()
        
        if evento == 'Menu Principal' or evento == 'Voltar':
            janelaInicial = Tela_Inicial(Id_User)

        elif evento == 'Cadastro' or evento == 'VoltarCadastro':
            janelaCadastro = Tela_Cadastro()

        elif evento == 'Login' or evento == 'Login...':
            janelaLogin = Tela_Login()

        elif evento == 'Inserir' or evento == 'INSERIR':
            janelaInserir = Tela_Inserir(matriz.getMatriz(), Id_User)
        
        elif evento == 'Ver Tudo' or evento == 'VER TUDO':
            janelaVerTudo = Tela_VerTudo(matriz.getMatriz(), Id_User)

        elif evento == 'Deletar' or evento == 'DELETAR':
            janelaDeletar = Tela_Deletar(matriz.getMatriz(), Id_User)

        elif evento == 'Consult Específica' or evento == 'CONSULTA ESPECÍFICA':
            janelaConsulta = Tela_Consulta(matriz.getMatriz(), Id_User)
            
        elif evento == 'Alterar' or evento == 'ALTERAR':
            janelaAlterar = Tela_Alterar(matriz.getMatriz(), Id_User)

        elif evento == 'Sobre...':
            Popup_Creditos()
        
        if (evento != 'Sobre...') and (evento not in ['Cadastro', 'VoltarCadastro']) and (evento not in ['Login', 'Login...']):
            matriz.Salvar_Matriz()
