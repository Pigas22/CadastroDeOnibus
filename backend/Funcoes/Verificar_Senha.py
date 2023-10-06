def Verificar_Senha(senha_Principal, senha_Confirmacao='', email_Login=''): # Fazer tratamento de erro
    from backend.Funcoes.Encriptador_Senhas import Encriptador_Senhas
    
    validacoes = 0
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    pontos = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',',  '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']

    if email_Login != '':
        with open('backend/BD_Contas/Todas_Contas.txt', 'r') as contas:
            todas_Contas = contas.readlines()
    
        contas.close()

        senha_Principal = Encriptador_Senhas(senha_Principal)

        for conta in todas_Contas:
            if email_Login in conta and senha_Principal in conta:
                return True

            else:
                return False
  
  
    else:
        if senha_Principal == senha_Confirmacao:
            validacoes += 1
      
            for numero in numeros:
                if numero in senha_Principal:
                    validacoes += 1
                    break
  
            for ponto in pontos:
                if ponto in senha_Principal:
                    validacoes += 1
                    break
  
    if validacoes == 3:
        return True
  
    else:
        return False
