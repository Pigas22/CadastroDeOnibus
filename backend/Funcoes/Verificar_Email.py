def Verificar_Email(email): # Fazer tratamento de erro
    with open('backend/BD_Contas/Todas_Contas.txt', 'r') as arquivo_emails:
        linhas = arquivo_emails.readlines()
    arquivo_emails.close()
  
    if linhas:
        for conta in linhas:
            Id_User = conta.split()[0]
            if email in conta:
                return False, Id_User

        return True
    
    else:
        return True
