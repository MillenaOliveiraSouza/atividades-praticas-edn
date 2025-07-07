"""
Exercicio 1: Crie uma  função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada.
Calcula o valor da gorjeta baseada no total a conta e na porcentagem desejada.
"""

def calcular_gorjeta(valor_conta, porcentagem):
    gorjeta = valor_conta * (porcentagem / 100)
    return gorjeta

conta = float(input("Valor da conta: R$ "))
porcent = float(input("Porcentagem da gorjeta (%): "))
print("Valor da gorjeta: R$", calcular_gorjeta(conta, porcent))
