"""
3 - Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. O arquivo CSV deve conter informações de pessoas, com colunas:
- Nome, Idade e Cidade.
"""

import csv

with open("pessoas.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print("Nome:", linha[0], "| Idade:", linha[1], "| Cidade:", linha[2])
