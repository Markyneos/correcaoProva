'''
Opções:
a) Apenas códgos A e B
b) Apenas códigos B e C
c) Apenas códigos A e C
d) Todos os códigos A, B e C
e) Nenhum dos códigos produz o mesmo resultado.
'''

#Código A:
lista = [x for x in range(5)]
print(lista) #[0, 1, 2, 3, 4]
#Código B:
lista = list(range(5))
print(lista) #[0, 1, 2, 3, 4]
#Código C:
lista = []
i = 0
while i < 5:
    lista.append(i)
    i += 1
print(lista) #[0, 1, 2, 3, 4]

#Resposta: Letra d.
#Relatório: Marquei em minha prova a letra d.
