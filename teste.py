from backend.Funcoes.Matriz import Matriz
from backend.Funcoes.Usuario import Usuario


Id_User = 1
matrizTeste = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

user = Usuario()
user.setIdUser(Id_User)

matriz = Matriz()
matriz.setIdUserMatriz(Id_User)
matriz.setMatriz(matrizTeste)
matriz.setContadorAlteracao()


matriz.LogMatriz(50)
