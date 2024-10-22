from random import randint
def print_matrix(mat):
  for row in mat:
    print(" ".join(str(n) for n in row))
#Matriz de teste:
matriz = [
    [randint(0, 9) for _ in range(3)],
    [randint(0, 9) for _ in range(3)],
    [randint(0, 9) for _ in range(3)]
]
print_matrix(matriz)
#Código a:
def soma_diagonal_principal(matriz: list[list]) -> int:
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma
print(f"Teste 1: {soma_diagonal_principal(matriz)}")
#Código b:
def soma_diagonal_principal2(matriz: list[list]) -> int:
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][-i]
    return soma
print(f"Teste 2: {soma_diagonal_principal2(matriz)}")
#Código c:
def soma_diagonal_principal3(matriz: list[list]) -> int:
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    return soma
print(f"Teste 3: {soma_diagonal_principal3(matriz)}")
#Código d:
def soma_diagonal_principal4(matriz: list[list]) -> int:
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][len(matriz) - i - 1]
    return soma
print(f"Teste 4: {soma_diagonal_principal4(matriz)}")
#Código e:
def soma_diagonal_principal5(matriz: list[list]) -> int:
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[len(matriz) - i - 1][i]
    return soma
print(f"Teste 5: {soma_diagonal_principal5(matriz)}")
#Resposta: letra a.
#Relatório: Marquei em minha prova a letra a.
