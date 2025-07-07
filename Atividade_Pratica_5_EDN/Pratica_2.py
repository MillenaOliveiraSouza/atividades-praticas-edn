"""
Exercicio 2: Crie uma função que calcule a idade de uma pessoa em dias, baseado no ano de nascimento.
"""

from datetime import date

def idade_em_dias(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade * 365 

ano = int(input("Ano de nascimento: "))
print("Idade aproximada em dias:", idade_em_dias(ano))
