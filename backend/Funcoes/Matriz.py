class Matriz():
    def __init__(self):
        self.__matriz = ''
        self.__Id_User = 0
        self.__contadorAlteracao = 0.1


    # Puxa o id do usuario
    def setIdUserMatriz(self, Id_User):
        self.__Id_User = Id_User


    # Contador de Alterações
    def setContadorAlteracao(self):
        try:
            alteracoes = []
            alteracao = []
            with open('backend\BD_Dados\LogDeAlterações.txt', 'r') as arquivoLog:
                linhas = arquivoLog.readlines()
                for linha in linhas:
                    if linha != '/' and linha != '/\n':
                        alteracao.append(linha)
                    
                    else:
                        alteracoes.append(alteracao)
                        alteracao = []
                        continue

                
                dados = alteracoes[-1]
                for dado in dados:
                    if dado == dados[0]:
                        self.__contadorAlteracao = float(dado.split()[2][0:3]) + 0.1
                        break

            arquivoLog.close()


        except FileNotFoundError:
            self.__contadorAlteracao = 0.1

    def getContadorAlteracao(self):
        return self.__contadorAlteracao

    
    # Inicializar matriz
    def Inicializar(self):
        with open(f'backend/BD_Dados/Usuario{self.__Id_User}_Dados.txt', 'rt') as arquivo:
            linhas = arquivo.readlines()
        arquivo.close()

        matriz = []

        if linhas:
            for i in range(0, len(linhas)):         
                linhas_espec = linhas[i].split()
                linha_inicial = []

                for itens in linhas_espec:
                    if '_' in itens:
                        quantDe_ = itens.count('_')

                        for underlines in range(0, quantDe_):
                            itens = itens.replace('_', ' ')

                    if itens.isnumeric():
                        linha_inicial.append(int(itens))

                    else:
                        linha_inicial.append(itens)


                matriz.append(linha_inicial)

        self.setMatriz(matriz)

    def setMatriz(self, matriz):
        self.__matriz = matriz

    def getMatriz(self):
        return self.__matriz


    # Inserir algo à Matriz
    def Inserir(self, motorista, linha, destino, qnt_passageiros):
        matriz = self.getMatriz()
        motorista = motorista.title()
        destino = destino.title()

        linhaMatriz = [motorista, linha, destino, qnt_passageiros]
        matriz.append(linhaMatriz)
        self.LogMatriz(f'Dados adicionados: [ {motorista}, {linha}, {destino}, {qnt_passageiros} ]')

        self.setMatriz(matriz)


    # Deleta uma linha na matriz ou ela inteira
    def Deletar(self, local_linha='', resetar= False):
        matriz = self.getMatriz()

        if resetar:
            for i in range(0, len(matriz)):
                matriz.pop()
            
            self.setMatriz(matriz)
            self.LogMatriz('Todos os dados foram apagados.')

        elif local_linha != '' :
            dado = matriz[local_linha]
            matriz.remove(dado)

            self.setMatriz(matriz)
            self.LogMatriz(f'Linha {local_linha + 1} foi apagada com sucesso. dados apagados: [ {" ".join(dado[0].split("_"))}, {dado[1]}, {" ".join(dado[2].split("_"))}, {dado[3]} ]')

        else:
            self.LogMatriz('Erro: não foi possível deletar o dado.')


    # Alterar dado na Matriz
    def Alterar_Dado(self, local_linha, local_coluna, novo_dado):
        from backend.Colunas import colunas

        matriz = self.getMatriz()
        coluna_final = colunas[local_coluna]
    
        matriz[local_linha][coluna_final] = novo_dado
        self.setMatriz(matriz)
        self.LogMatriz(f'Dados alterados com sucesso! \nDados da alteração: \n    - Linha: {local_linha} \n    - Coluna: {local_coluna} \n    - Novo Dado: {novo_dado}')

    
    # Salvar Matriz
    def Salvar_Matriz(self):
        matriz = self.getMatriz()
        for linha in matriz:
            if ' ' in linha[0]:
                linha[0] = '_'.join(linha[0].split())

            if ' ' in linha[2]:
                linha[2] = '_'.join(linha[2].split())


        with open(f'backend/BD_Dados//Usuario{self.__Id_User}_Dados.txt', 'w') as arquivo:
            for linhas in matriz:
                for itens in linhas:
                    arquivo.write(f'{itens} ')
                arquivo.write('\n')

        arquivo.close()
  
        self.LogMatriz('Informações salvas com sucesso!')


    # Log de alterações na matriz
    def LogMatriz(self, alteracao):
        import datetime

        
        arquivoExiste = False
        with open('backend\BD_Contas\Todas_Contas.txt', 'r') as arquivo_contas:
            linhas = arquivo_contas.readlines()
        arquivo_contas.close()

        for conta in linhas:
            if int(conta[0]) == self.__Id_User:
                dados = conta.split()
                break

        nomeUser = dados[1]
        emailUser = dados[2]
        data_horario = datetime.datetime.now().strftime('%d/%m/%Y | %H:%M')

        try:
            arquivoLog = open(f'backend/BD_Dados/LogDeAlterações.txt', 'x+')

        except FileExistsError:
            arquivoLog = open(f'backend/BD_Dados/LogDeAlterações.txt', 'a')
            arquivoExiste = True

        finally:
            if arquivoExiste:
                arquivoLog.write(f"\n==================== Log {self.__contadorAlteracao:.1f}v ====================")

            else:
                arquivoLog.write(f"==================== Log {self.__contadorAlteracao:.1f}v ====================")

            arquivoLog.write(f"\nData e Horário: {data_horario}" +
                             f"\nUsuário: {nomeUser}" +
                             f"\nContato: {emailUser}" +
                             "\n" +
                             "\n- Alteração:" +
                             f"\n    {alteracao}" + 
                             "\n" +
                             "\n/")

            arquivoLog.close()

        self.__contadorAlteracao += 0.1
