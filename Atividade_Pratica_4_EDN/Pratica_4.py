"""
Exercicio 4: Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização.
Utilize a API da AwesomeAPI para obter os dados de cotação.​
"""

import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()

url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
resposta = requests.get(url)
dados = resposta.json()

chave = moeda + "BRL"

if chave in dados:
    info = dados[chave]
    print("Moeda:", moeda)
    print("Valor atual:", info['bid'])
    print("Valor mínimo:", info['low'])
    print("Valor máximo:", info['high'])
    print("Última atualização:", info['create_date'])
else:
    print("Moeda inválida ou não encontrada!")
