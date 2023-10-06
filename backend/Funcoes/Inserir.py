def Inserir(matriz, motorista, linha, destino, quant_passageiros):
    motorista = motorista.title()
    destino = destino.title()
    
    linha = [motorista, linha, destino, quant_passageiros]
    matriz.append(linha)
