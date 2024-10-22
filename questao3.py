'''
3) (0,5) Observe a função recursiva ao lado. Qual é a saída ao executar este código?
a) 3
b) 6
c) 9
d) 0
e) Erro de recursão infinita
'''
def func(n: int) -> int:
    if n ==0:
        return 1
    else:
        return n * func(n - 1)

print(func(3)) # 6
#Resposta: letra b.
#Relatório: A resposta que marquei em minha prova foi a letra b.
