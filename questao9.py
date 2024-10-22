if __name__ == '__main__':
    alpha = float(input('Informe alpha: '))
    x = float(input('Informe x: '))
    if alpha > 0.1:
        print("Valor inválido para alpha")
    else:
        if x < 0:
            print(alpha * x)
        else:
            print(x)


'''
O código apresentado vai produzir a saída adequada para todas as diferentes entradas de alpha e x? Justifique
apresentando o teste de mesa contendo as diferentes combinações de entradas e suas respectivas saídas.

Teste de mesa:

  Alpha  |  X  |         Resultado         |
   0.5   | -5  | Valor inválido para Alpha |
   0.05  | -5  |           -0.25           |
   0.05  |  2  |             2             |

'''

