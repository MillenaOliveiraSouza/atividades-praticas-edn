"""
2 - Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas, com colunas:
- Nome, Idade e Cidade.
"""

import csv

pessoas = [
    ["Nome", "Idade", "Cidade"],
    ["Ana", 25, "Campinas"],
    ["Bruno", 30, "São Paulo"],
    ["Clara", 22, "Rio de Janeiro"]
]

with open("pessoas.csv", "w", newline="") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerows(pessoas)

print("Arquivo CSV criado com sucesso!")
