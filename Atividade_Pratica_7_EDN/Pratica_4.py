"""
4 -  Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos:
- Nome, Idade e Cidade.
"""

import json

pessoa = {
    "Nome": "Millena",
    "Idade": 24,
    "Cidade": "Campinas"
}

with open("pessoa.json", "w") as arquivo:
    json.dump(pessoa, arquivo, indent=4)

with open("pessoa.json", "r") as arquivo:
    dados = json.load(arquivo)
    print("Nome:", dados["Nome"])
    print("Idade:", dados["Idade"])
    print("Cidade:", dados["Cidade"])
