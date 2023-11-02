class Usuario():
    def __init__(self):
        self.__id = "" # ID - cadastro e login
        self.__nome = "" # Nome - cadastro
        self.__email = "" # Email - cadastro
        self.__loginEmail = "" # Email - login
        self.__emailVerificado = False
        self.__senha1 = "" # Senha Pricipal - cadastro
        self.__senha2 = "" # Senha de Confirmação - cadastro
        self.__loginSenha = "" # Senha - login
        self.__senhaVerificada = False
        self.__senhaDesencriptada = "" # Senha para ser vista nas configurações da conta
    
    # ID
    def setIdUser(self, id_User= 1, login= False):
        if login:
            with open('backend\BD_Contas\Todas_Contas.txt', 'r') as arquivo_Contas:
                linhas = arquivo_Contas.readlines()
            arquivo_Contas.close()

            for contas in linhas:
                if self.getLoginEmailUser() in contas:
                    self.__id = int(contas[0])
                    break

        else:
            self.__id = int(id_User)
    
    def getIdUser(self):
        return self.__id

    
    # Nome
    def setNomeUser(self, nome_User):
        self.__nome = nome_User
    
    def getNomeUser(self):
        return self.__nome

    
    # Email
    def setEmailUser(self, email_User):
        self.__email = email_User

    def getEmailUser(self):
        return self.__email
        
    def setLoginEmailUser(self, loginEmail_User):
        self.__loginEmail = loginEmail_User

    def getLoginEmailUser(self):
        return self.__loginEmail
    
    def setEmailVerificado(self, email_Verificado):
        self.__emailVerificado = email_Verificado
        
    def getEmailVerificado(self):
        return self.__emailVerificado
        
    def verificarEmail(self, atualizar_dado= False, novo_email=''): # Fazer tratamento de erro
        from interface.Popup_Padrao import Popup_Padrao
        email = self.getEmailUser()
        email_Login = self.getLoginEmailUser()

        if (email.find("@") != -1 and email != '') or (email_Login.find("@") != -1 and email_Login != '') or (novo_email.find("@") != -1 and novo_email != ''):
            with open('backend/BD_Contas/Todas_Contas.txt', 'r') as arquivo_emails:
                linhas = arquivo_emails.readlines()
            arquivo_emails.close()
    
            if linhas:
                for conta in linhas:
                    if atualizar_dado: # Atualização do Email
                        if novo_email in conta:
                            self.setEmailVerificado(False)
                            break

                        else:
                            self.setEmailVerificado(True)


                    elif email_Login == '': # Cadastro
                        if email in conta:
                            self.setEmailVerificado(False)
                            break

                        else:
                            self.setEmailVerificado(True)


                    # Login
                    else:
                        if email_Login in conta:
                            self.setEmailVerificado(True)
                            break

                        else:
                            self.setEmailVerificado(False)

            else:
                self.setEmailVerificado(True)

        else:
            Popup_Padrao("ERROR: Email Inválido" , "Por favor, digite um email válido.")


    # Senhas
    def setSenha1User(self, senha1_User):
        self.__senha1 = self.__encriptadorSenhas(senha1_User)
    
    def getSenha1User(self):
        return self.__senha1

    def setSenha2User(self, senha2_User): 
        self.__senha2 = self.__encriptadorSenhas(senha2_User)
    
    def getSenha2User(self):
        return self.__senha2

    def setLoginSenhaUser(self, loginSenha_User):
        self.__loginSenha = self.__encriptadorSenhas(loginSenha_User)

    def getLoginSenhaUser(self):
        return self.__loginSenha

    def setSenhaVerificada(self, senha_Verificada):
        self.__senhaVerificada = senha_Verificada

    def getSenhaVerificada(self):
        return self.__senhaVerificada

    def setSenhaDesencripatada(self):
        senha_Desencripitada = self.getSenha1User()
        if senha_Desencripitada == '':
            senha_Desencripitada = self.getLoginSenhaUser()

        self.__senhaDesencriptada = self.__encriptadorSenhas(senha_Desencripitada, reverse= True)

    def getSenhaDesencriptada(self):
        return self.__senhaDesencriptada

    def verificarSenha(self, atualizar_dado= False, nova_senha= ''): # Fazer tratamento de erro
        validacoes = 0
        numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        pontos = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',',  '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']

        email_Login = self.getLoginEmailUser()
        if atualizar_dado:
            senha_Principal = nova_senha
            for numero in numeros:
                if numero in senha_Principal:
                    validacoes += 1
                    break

            for ponto in pontos:
                if ponto in senha_Principal:
                    validacoes += 1
                    break

            if validacoes == 2:
                self.setSenhaVerificada(True)
    
            else:
                self.setSenhaVerificada(False)


        elif email_Login != '': # Login
            with open("backend/BD_Contas/Todas_Contas.txt", 'r') as arquivo:
                linhas = arquivo.readlines()
            arquivo.close()

            for conta in linhas:
                if self.getLoginSenhaUser() in conta and email_Login in conta:
                    self.setSenhaVerificada(True)
                    break

                else:
                    self.setSenhaVerificada(False)


        else:
            senha_Principal = self.getSenha1User() 
            senha_Confirmacao = self.getSenha2User()
            
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
                self.setSenhaVerificada(True)
    
            else:
                self.setSenhaVerificada(False)


    def __encriptadorSenhas(self, senha, reverse= False):
        encriptacao = {
            # conter todas as caracteres possiveis para fazer a encriptação
            '1': '##', '2': '#0', '3': '#1', '4': '#2', '5': '#3', '6': '#4', 
            '7': '#5', '8': '#6', '9': '#7', '0': '#8', ' ': '#9', '!': '0#', 
            '"': '00', '#': '01', '$': '02', '%': '03', '&': '04', "'": '05',
            '(': '06', ')': '07', '*': '08', '+': '09', ',': '1#', '-': '10',
            '.': '11', '/': '12', ':': '13', ';': '14', '<': '15', '=': '16',
            '>': '17', '?': '18', '@': '19', '[': '2#', ']': '20', '^': '21', 
            '_': '22', '`': '23', '{': '24', '|': '25', '}': '26', '~': '27',
            'a': '28', 'b': '29', 'c': '3#', 'd': '30', 'e': '31', 'f': '32',
            'g': '33', 'h': '34', 'i': '35', 'j': '36', 'k': '37', 'l': '38',
            'm': '39', 'n': '4#', 'o': '40', 'p': '41', 'q': '42', 'r': '43',
            's': '44', 't': '45', 'u': '46', 'v': '47', 'w': '48', 'x': '49',
            'y': '5#', 'z': '50', 'A': '51', 'B': '52', 'C': '53', 'D': '54',
            'E': '55', 'F': '56', 'G': '57', 'H': '58', 'I': '59', 'J': '6#',
            'K': '60', 'L': '61', 'M': '62', 'N': '63', 'O': '64', 'P': '65',
            'Q': '66', 'R': '67', 'S': '68', 'T': '69', 'U': '7#', 'V': '70',
            'W': '71', 'X': '72', 'Y': '73', 'Z': '74'
        }

        if reverse:
            senha_Desencriptada = ''
            for letra in range(0, len(senha), 2):
                for keys, values in encriptacao.items():
                    if (senha[letra] + senha[letra+1]) == values:
                        senha_Desencriptada += keys

            return senha_Desencriptada

        else:
            senha_Encriptada = ''
            for letra in senha:
                senha_Encriptada += encriptacao[letra]

            return senha_Encriptada

    
    # Conta    
    def salvarConta(self, atualizar_nome= False, atualizar_email= False, atualizar_senha= False):
        nome_Completo = '_'.join(self.getNomeUser().split())

        with open('backend/BD_Contas/Todas_Contas.txt', 'r') as arquivo_Contas:
            linhas = arquivo_Contas.readlines()

        arquivo_Contas.close()

        if not atualizar_nome and not atualizar_email and not atualizar_senha:
            with open('backend/BD_Contas/Todas_Contas.txt', 'a') as arquivo_Contas2:
                if linhas:
                    arquivo_Contas2.write(f'\n{self.getIdUser()} {nome_Completo} {self.getEmailUser()} {self.getSenha1User()}')

                else:
                    arquivo_Contas2.write(f'{self.getIdUser()} {nome_Completo} {self.getEmailUser()} {self.getSenha1User()}')

            arquivo_Contas2.close()

        
        else:
            email = self.getEmailUser()
            if email == '':
                email = self.getLoginEmailUser()

            senha = self.getSenha1User()
            if senha == '':
                senha = self.getLoginSenhaUser()

            Id_User = self.getIdUser()

            with open('backend/BD_Contas/Todas_Contas.txt', 'w') as arquivo_Contas3:
                for conta in linhas:
                    dados = conta.split()

                    if int(dados[0]) == Id_User:
                        if atualizar_nome:
                            dados[1] = nome_Completo

                        elif atualizar_email:
                            dados[2] = email

                        elif atualizar_senha:
                            dados[3] = senha

                        if conta != linhas[0]:
                            arquivo_Contas3.write(f'\n{" ".join(dados)}')
                        
                        else:
                            arquivo_Contas3.write(f'{" ".join(dados)}')

                    else:
                        if conta != linhas[0]:
                            arquivo_Contas3.write(f'\n{dados[0]} {dados[1]} {dados[2]} {dados[3]}')
                        
                        else:
                            arquivo_Contas3.write(f'{dados[0]} {dados[1]} {dados[2]} {dados[3]}')

            arquivo_Contas3.close()

        return 'Conta salva com sucesso!!'
