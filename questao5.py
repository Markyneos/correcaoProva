'''
5) (1,0) Considere o seguinte problema: Dada uma lista de números inteiros, verificar se existem elementos duplicados na lista. A seguir, são apresentadas três diferentes abordagens em Python para resolver esse problema:
a) Abordagem 1 é mais eficiente em tempo e espaço
b) Abordagem 2 é mais eficiente em tempo, mas consome mais espaço
c) Abordagem 3 é mais eficiente em tempo, mas consome mais espaço
d) Abordagem 1 é mais eficiente em espaço, mas menos eficiente em tempo
e) Abordagem 2 é mais eficiente em espaço, mas menos eficiente em tempo
'''
from random import randint
import time
import sys


lista = [randint(1, 1000) for _ in range(100000)]


#Solução 1:
def tem_duplicados1(lista: list) -> bool:
    start = time.time()
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                end = time.time()
                totalTime = end - start
                print(f"Espaço utilizado: {sys.getsizeof(lista)}")
                print(f"Tempo gasto: {totalTime:.7f}")
                return True
    end = time.time()
    totalTime = end - start
    print(f"Espaço utilizado: {sys.getsizeof(lista)}")
    print(f"Tempo gasto: {totalTime:.7f}")
    return False
print(tem_duplicados1(lista))
print("\n")


#Solução 2:
def tem_duplicados2(lista: list) -> bool:
    start = time.time()
    lista_ordenada = sorted(lista)
    for i in range(len(lista_ordenada) - 1):
        if lista_ordenada[i] == lista_ordenada[i + 1]:
            end = time.time()
            totalTime = end - start
            print(f"Espaço utilizado: {sys.getsizeof(lista) + sys.getsizeof(lista_ordenada)}")
            print(f"Tempo gasto: {totalTime:.7f}")
            return True
    end = time.time()
    totalTime = end - start
    print(f"Espaço utilizado: {sys.getsizeof(lista) + sys.getsizeof(lista_ordenada)}")
    print(f"Tempo gasto: {totalTime:.7f}")
    return False
print(tem_duplicados2(lista))
print("\n")


#Solução 3:
def tem_duplicados3(lista: list) -> bool:
    start = time.time()
    elementos_vistos = set()
    for elemento in lista:
        if elemento in elementos_vistos:
            end = time.time()
            totalTime = end - start
            print(f"Espaço utilizado: {sys.getsizeof(lista) + sys.getsizeof(elementos_vistos)}")
            print(f"Tempo gasto: {totalTime:.7f}")
            return True
        elementos_vistos.add(elemento)
    end = time.time()
    totalTime = end - start
    print(f"Espaço utilizado: {sys.getsizeof(lista) + sys.getsizeof(elementos_vistos)}")
    print(f"Tempo gasto: {totalTime:.7f}")
    return False
print(tem_duplicados3(lista))


'''
Resposta: letra b, c e d, de acordo com as saídas. Gabarito: Letra c e d.

Explicação: A abordagem 1 consome menos espaço em comparação às outras, pois tem uma lista, enquanto o resto
cria uma lista e um set e uma lista e sua cópia. Em tempo, a solução 3 é mais eficiente, porque realiza somente
uma iteração, enquanto as outras realizam no mínimo duas, e é possível ver as provas disto pela função time em
cada definição de função. A solução 2, como diz a alternativa b, é mais eficiente em tempo do que sua eficiência em espaço,
porque ocupa mais espaço armazenando duas listas, mas ela faz somente uma iteração sobre elas.

Execução do código: Quando executo o código, as minhas saídas afirmam que a solução 2 ocupa mais tempo e espaço que as outras
duas, enquanto a primeira consome um pouco mais de tempo que a segunda e menos espaço que as duas, e a terceira um pouco mais
de espaço que a primeira e um pouco menos de tempo.

Relatório: Marquei a letra d em minha prova, pois estava certo pra mim que a solução 3 levaria menos tempo, por realizar
uma iteração somente, e mais espaço por usar um set e a lista original.
'''
