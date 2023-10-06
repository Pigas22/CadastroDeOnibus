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
