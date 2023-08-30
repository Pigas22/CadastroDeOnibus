colunas = {
    'Motorista': 0,
    'Linha': 1,
    'Destino': 2,
    'Passageiro': 3
}

colunas_inversa = {
    '0': 'Id',
    '1': 'Motorista',
    '2': 'Linha',
    '3': 'Destino',
    '4': 'Passageiro'
}


def Inicializar(Id_User):
    # colocar assim que abrir o app, para puxar as informações do arquivo.    
    with open(f'backend/BD_Dados/Usuario{Id_User}_Dados.txt', 'rt') as arquivo:
        linhas = arquivo.readlines()
    arquivo.close()

    matriz = []
  
    if linhas:
        for i in range(0, len(linhas)):
            linhas_espec = linhas[i].split() # linhas_espec = [motoristaN, linhaX, destinoY, quantidade_pass.Z]
            linha_inicial = []
      
            for itens in linhas_espec:
                if '_' in itens:
                    quantDe_ = itens.count('_')
                    for underlines in range(0, quantDe_):
                        itens = itens.replace('_', ' ')

            try:
                linha_inicial.append(int(itens))
          
            except ValueError:         
                linha_inicial.append(itens)
      
            matriz.append(linha_inicial)

    return matriz


def Salvar(matriz, Id_User):
    for linha in matriz:
        if ' ' in linha[0]:
            linha[0] = '_'.join(linha[0].split())
  
        if ' ' in linha[2]:
            linha[2] = '_'.join(linha[2].split())
    
    with open(f'backend/BD_Dados/Usuario{Id_User}_Dados.txt', 'w') as arquivo:
        for linhas in matriz:
            for itens in linhas:
                arquivo.write(f'{itens} ')
            arquivo.write('\n')
  
    arquivo.close()
  
    return 'Informações salvas com sucesso!'

  
def Mostrar_Tudo(matriz):
    # Não será necessário.
    for i in matriz:
        for item in i:
            print(f'| {item}', end=' | ')
        
        print()
    

def Deletar(matriz, local_linha='', resetar=False):
    if resetar:
        # reseta toda a matriz
        matriz = []

        return 'Todos os dados foram apagados.'

    elif local_linha != '' :
        #Deleta uma linha em específico
        dado = matriz[local_linha]
        matriz.remove(dado)
    

        return f'Linha {local_linha + 1} foi apagada com sucesso. [ {dado} ]'

    else:
        return 'Erro!'


def Consulta_Espec(matriz, local_linha=''):
    """
        A função retornará uma linha inteira.

        Exemplo:
            print(consulta_espec(matriz, 3,)) == [26, 27, 28, 29, 30]
    """
    
    try:
        dados = []
        tamanho = len(matriz[local_linha])
        for item in range(0, tamanho):
            dados.append(matriz[local_linha][item])


    except Exception as ERROR:
        return f'Erro do tipo: {ERROR.__cause__}'

    else:
        return dados


def Inserir(matriz, motorista, linha, destino, quant_passageiros):
    motorista = motorista.title()
    
    linha = [motorista, linha, destino, quant_passageiros]
    matriz.append(linha)


def Alterar_Dado(matriz, local_linha, local_coluna, novo_dado):
    global colunas

    local_coluna = colunas[local_coluna]
  
    if ' ' in novo_dado:
        novo_dado = '_'.join(novo_dado.split())
    
    matriz[local_linha][local_coluna] = novo_dado


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


def Verificar_Senha(senha_Principal, senha_Confirmacao='', email_Login=''): # Fazer tratamento de erro 
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


def Salvar_Contas(Id_User, nome_Completo, email, senha_Principal):
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


def Encriptador_Senhas(senha):
    # a ser desenvolvido
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

    senha_Encriptada = ''
    for letra in senha:
        senha_Encriptada += encriptacao[letra]
 
    return senha_Encriptada
  