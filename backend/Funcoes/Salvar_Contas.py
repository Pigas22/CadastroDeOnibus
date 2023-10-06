def Salvar_Contas(Id_User, nome_Completo, email, senha_Principal):
    from backend.Funcoes.Encriptador_Senhas import Encriptador_Senhas
    
    
    nome_Completo = '_'.join(nome_Completo.split())
    senha_Encriptada = Encriptador_Senhas(senha_Principal)
  
    with open('backend/BD_Contas/Todas_Contas.txt', 'r') as arquivo_Contas:
        linhas = arquivo_Contas.readlines()
    
    arquivo_Contas.close()
    
    with open('backend/BD_Contas/Todas_Contas.txt', 'a') as arquivo_Contas2:
        if linhas:
            arquivo_Contas2.write(f'\n{Id_User} {nome_Completo} {email} {senha_Encriptada}')

        else:
            arquivo_Contas2.write(f'{Id_User} {nome_Completo} {email} {senha_Encriptada}')
            
    arquivo_Contas2.close()

    return 'Conta salva com sucesso!'
