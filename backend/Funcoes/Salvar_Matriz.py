def Salvar_Matriz(matriz, Id_User):
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
