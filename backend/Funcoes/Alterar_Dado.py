def Alterar_Dado(matriz, local_linha, local_coluna, novo_dado):
    from backend.Colunas import colunas

    local_coluna = colunas[local_coluna]
  
    if ' ' in novo_dado:
        novo_dado = '_'.join(novo_dado.split())
    
    matriz[local_linha][local_coluna] = novo_dado
