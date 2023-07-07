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


def inicializar():
  # colocar assim que abrir o app, para puxar as informações do arquivo.    
  with open('backend/matriz.txt', 'rt') as arquivo:
    linhas = arquivo.readlines()
  arquivo.close()

  matriz = []
  
  if linhas:
    for i in range(0, len(linhas)):
      linhas_espec = linhas[i].split() # linhas_espec = [sas, 700, 700, 700]
      linha_inicial = []
      
      for itens in linhas_espec:
        try:
          linha_inicial.append(int(itens))
          
        except ValueError:
          linha_inicial.append(itens)
      
      matriz.append(linha_inicial)

  return matriz


def salvar(matriz):
  # Colocar no final do código, para salvar as informações. 
  with open('backend/matriz.txt', 'w') as arquivo:
    for linhas in matriz:
      for itens in linhas:
        arquivo.write(f'{itens} ')
      arquivo.write('\n')
  
  arquivo.close()
  
  return 'Informações salvas com sucesso!'

  
def mostrar_tudo(matriz):
  # Não será necessário.
  for i in matriz:
    for item in i:
      print(f'| {item}', end=' | ')

    print()
    

def deletar(matriz, local_linha='', resetar=False):
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


def consulta_espec(matriz, local_linha='', linha=False):
  """
  Quando,
    | linha = True:
      A função retornará uma linha inteira.

      Exemplo:
        print(consulta_espec(matriz, 3, linha=True)) == [26, 27, 28, 29, 30]
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


def inserir(matriz, motorista, linha, destino, passageiros):
  if ' ' in motorista:
    motorista = '_'.join(motorista.split())
    
  linha = [motorista, linha, destino, passageiros]
  matriz.append(linha)


def alterar_dado(matriz, local_linha, local_coluna, novo_dado):
  global colunas

  local_coluna = colunas[local_coluna]
  
  if ' ' in novo_dado:
    novo_dado = '_'.join(novo_dado.split())
    
  matriz[local_linha][local_coluna] = novo_dado
