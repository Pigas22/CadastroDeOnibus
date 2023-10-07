import PySimpleGUI as sg
from backend import Colunas_Inversa
from backend.Funcoes import Verificar_Email, Verificar_Senha, Salvar_Contas, Salvar_Matriz, Inicializar, Inserir, Deletar, Alterar_Dado
from interface.Tela_Cadastro import Tela_Cadastro #
from interface.Tela_Login import Tela_Login #
from interface.Tela_Inicial import Tela_Inicial #
from interface.Tela_Inserir import Tela_Inserir #
from interface.Tela_VerTudo import Tela_VerTudo #
from interface.Tela_Deletar import Tela_Deletar #
from interface.Tela_Consulta import Tela_Consulta # 
from interface.Tela_Alterar import Tela_Alterar #
from interface.Popup_Creditos import Popup_Creditos
from interface.Tela_PerfilUser import Tela_PerfilUser # Vou usar ainda
from interface.Op_MenuBAR import op_menuBar


detalhes = {
    'corFundo': 'SlateBlue',
    'tema': 'DarkBlue',
    'fonte': 'Arial',
    'tamanhoFonte': '12',
    'corTexto': 'Black'
}

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

matriz = []

while True:
    window, evento, valor = sg.read_all_windows()

    """
    print(f'JANELA: {window}')
    print(f'EVENTO: {evento}')
    print(f'VALOR: {valor}')
    print('======================================================')
    """

    if window == janelaCadastro:
        validacoes = 0
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            janelaCadastro.close()
            break

        if evento == 'Login' or evento == 'Login...':
            janelaCadastro.close()
            janelaLogin = Tela_Login()

        elif evento == 'Salvar Dados' or evento == 'KP_Enter:104' or evento == 'Return:36':
            nome_Completo = valor['Nome_Completo'] 
            email = valor['Email']
            senha_Principal = valor['Senha_Principal']
            senha_Confirmacao = valor['Senha_Confirmação']
            
            email_valido = Verificar_Email.Verificar_Email(email)
            senha_valida = Verificar_Senha.Verificar_Senha(senha_Principal, senha_Confirmacao)

            if senha_valida and email_valido: 
                # varifica a senha e o email se estao devidamente corretos
                validacoes += 2

            elif not email_valido:
                sg.popup('Email já cadastrado anteriormente!', 'O email informado já está vinculado a uma conta, por favor, informe outro endereço de email ou logue na conta.', background_color='Slate Blue')
      
            elif not senha_valida:
                sg.popup('Senha incorreta!', 'As senhas informadas não coincidem ou A senha está fraca. \n| As senhas devem conter números e caracteres especiais, como: ! @ # ( : *.', background_color='Slate Blue')

            if validacoes == 2:
                with open('backend/BD_Contas/Todas_Contas.txt', 'r') as arquivo:
                    linhas = len(arquivo.readlines())
                arquivo.close()

                Id_User = linhas + 1 

                with open(f'backend/BD_Dados/Usuario{Id_User}_Dados.txt', 'xt') as arquivo:
                    arquivo.close()

                Salvar_Contas.Salvar_Contas(Id_User, nome_Completo, email, senha_Principal)
               
                sg.popup('Conta criada com sucesso!!', 'Parabéns, agora você pode utilizar o programa com sua conta e ter seus dados salvos.', background_color=  'SlateBlue')
        
                janelaCadastro.close()
                matriz = Inicializar.Inicializar(Id_User)
                janelaInicial = Tela_Inicial(Id_User)
                

            elif evento == 'Limpar':
                lacunas = [janelaCadastro['Nome_Completo'], janelaCadastro['Email'], janelaCadastro['Senha_Principal'], janelaCadastro['Senha_Confirmação']]
                for lacuna in lacunas:
                    lacuna.update('')

    
    elif window == janelaLogin:
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            janelaLogin.close()
            break

        elif evento == 'Cadastro':
            janelaLogin.close()
            janelaCadastro = Tela_Cadastro()

        elif evento == 'Fazer Login' or evento == 'KP_Enter:104' or evento == 'Return:36':
            validacao = 0

            email_Login = valor['Email_Login']
            senha_Login = valor['Senha_Login']
      
            if email_Login and senha_Login:
                email_Valido = Verificar_Email.Verificar_Email(email_Login)
                Id_User = email_Valido[1]
                if email_Valido[0]:
                    sg.popup('Email incorreto!', 'O email informado não está vinculado à nenhuma conta', background_color=detalhes['corFundo'])
    
                else:
                    validacao += 1
    
                senha_Valida = Verificar_Senha.Verificar_Senha(senha_Login, email_Login=email_Login)
                if senha_Valida:
                    validacao += 1
    
                else:
                    sg.popup('Senha Incorreta!', 'Por favor, digite-a novamente.', background_color=detalhes['corFundo'])
              
    
                if validacao == 2:
                    sg.popup('Login Efetuado com Sucesso!', 'Aproveite o App.', background_color=detalhes['corFundo'])
                    janelaLogin.close()
                    matriz = Inicializar.Inicializar(Id_User)
                    janelaInicial = Tela_Inicial(Id_User)
              
    
            else:
                sg.popup('Email e senha não informados!', 'Por favor, informe-os para efetuar o login.')

        elif evento == 'Limpar':
            lacunas = [janelaLogin['Email_Login'], janelaLogin['Senha_Login']]
            for lacuna in lacunas:
                lacuna.update('')

    
    elif window == janelaInicial:
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            break

    
    elif window == janelaInserir:
        if evento == sg.WINDOW_CLOSED:
            janelaInserir.close()
            janelaInicial = Tela_Inicial(Id_User)
      
        if evento == 'Cadastrar':
            motorista = valor['motorista']    
            linha = valor['linha']
            destino = valor['destino']
            quant_passageiros = valor['N° de PASSAGEIROS']
    
            Inserir.Inserir(matriz, motorista, linha, destino, quant_passageiros)

            sg.popup('Viagem adicionada com sucesso!', 'Confira a nova adição na tela "Ver Tudo".', background_color= detalhes['corFundo'], any_key_closes= True, text_color= 'White')
    

    elif window == janelaVerTudo:
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            janelaVerTudo.close()
            janelaInicial = Tela_Inicial(Id_User) 
            

    elif window == janelaDeletar:
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            janelaDeletar.close()
            janelaInicial = Tela_Inicial(Id_User)

        elif evento[0] == 'tabela_atual':
            selected_id = janelaDeletar['ID']
            selected_id.update(evento[2][0])
            valor['ID'] = evento[2][0]

        elif evento == 'CONFIRMAR':
            id_do_registro = int(valor['ID'])
            
            Deletar.Deletar(matriz, local_linha= id_do_registro)
            tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz)]
            
            tabela = janelaDeletar['tabela_atual']
            tabela.update(values=tabela_comId)
            
            sg.popup_auto_close('Operação bem-sucedida', 'Valor deletado com sucesso! ', background_color= detalhes['corFundo'], text_color= detalhes['corTexto'], font='Arial 12')
            resp_delete = janelaDeletar['ID']
            resp_delete.update('')

    
    elif window == janelaConsulta:
        filtro = 'id'
        filtros_Keys = ['FILTRO_ID', 'FILTRO_MOTORISTA', 'FILTRO_LINHA', 'FILTRO_DESTINO', 'FILTRO_PESSOAS']
    
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            janelaConsulta.close()
            janelaInicial = Tela_Inicial(Id_User)

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
                        matriz_Pesquisa.append(matriz[int(chave_pesquisa)])

                    except ValueError:
                        sg.popup('Error:', 'Informe apenas o ID do Ônibus', background_color=  detalhes['corFundo'])
    
                else:
                    for linha in matriz:
                        if linha[filtro] == chave_pesquisa:
                            matriz_Pesquisa.append(linha)

                    if len(matriz_Pesquisa) == 0:
                        sg.popup('Error: ', 'Não possui esse dado no Banco', background_color= detalhes['corFundo'])
    
                tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz_Pesquisa)]
                janelaConsulta['tabela'].update(values=tabela_comId)

                janelaConsulta['KEY_PESQUISA'].update('')


            except IndexError:
                sg.popup('Error: ', 'Não possui esse dado no Banco', background_color=  detalhes['corFundo'])
        
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
            tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz)]
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
      
        elif evento == 'CONFIRMAR':
            ID_linha = valor['ID_linha']
            ID_coluna = valor['ID_coluna']
            new_dado = valor['NOVO_DADO']
      
            Alterar_Dado.Alterar_Dado(matriz, ID_linha, ID_coluna, new_dado)
            Salvar_Matriz.Salvar_Matriz(matriz, Id_User)
      
            tabela_comId = [[i] + sublist for i, sublist in enumerate(matriz)]
            tabela = janelaAlterar['tabela']
            tabela.update(values=tabela_comId)
      
            sg.popup_auto_close('Operação bem-sucedida', 'Valor alterado com sucesso! ', background_color='Slate Blue', text_color= detalhes['corTexto'], font=f'{ detalhes["fonte"]} { detalhes["tamanhoFonte"]}')
            resposta = janelaAlterar['NOVO_DADO']
            resposta.update('')

    
    if evento in op_menuBar:    
        window.close()
        
        if evento == 'Menu Principal':
            janelaInicial = Tela_Inicial(Id_User)

        elif evento == 'Inserir' or evento == 'INSERIR':
            janelaInserir = Tela_Inserir(matriz, Id_User)
        
        elif evento == 'Ver Tudo' or evento == 'VER TUDO':
            janelaVerTudo = Tela_VerTudo(matriz, Id_User)

        elif evento == 'Deletar' or evento == 'Deletar':
            janelaDeletar = Tela_Deletar(matriz, Id_User)

        elif evento == 'Consult Específica' or evento == 'CONSULTA ESPECÍFICA':
            janelaConsulta = Tela_Consulta(matriz, Id_User)
            
        elif evento == 'Alterar' or evento == 'ALTERAR':
            janelaAlterar = Tela_Alterar(matriz, Id_User)

        elif evento == 'Sobre...':
            Popup_Creditos()

        Salvar_Matriz.Salvar_Matriz(matriz, Id_User)
