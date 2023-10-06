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

                if itens.isnumeric():
                    linha_inicial.append(int(itens))
                    
                else:
                    linha_inicial.append(itens)
                
            
            matriz.append(linha_inicial)

    return matriz
