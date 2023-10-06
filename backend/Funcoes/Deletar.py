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
