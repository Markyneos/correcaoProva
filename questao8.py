#a) Calcule e informe o IMC de uma pessoa.
def calcularImc(altura: float, peso: float) -> float:
    return peso / (altura ** 2)

#b) Informe a classificação, segundo a OMS, da pessoa.
def classificarImc(peso: float, altura: float) -> str:
    imc = peso / (altura ** 2)
    if imc < 17:
        return "Muito abaixo do peso"
    elif imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade Grau I"
    elif imc < 40:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

#inputs para o output:
peso = float(input("Insira seu peso (em kilos): "))
altura = float(input("Insira sua altura (em metros): "))
print(f"IMC: {calcularImc(altura, peso):.2f}")
print(f"Classificação: {classificarImc(peso, altura)}")
