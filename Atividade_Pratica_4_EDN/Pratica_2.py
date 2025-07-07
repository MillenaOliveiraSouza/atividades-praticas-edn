"""
Exercicio 2: Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'.
O programa deve exibir o nome, email e país do usuário gerado.
"""

import requests

resposta = requests.get("https://randomuser.me/api/")
dados = resposta.json()

nome = dados['results'][0]['name']['first'] + " " + dados['results'][0]['name']['last']
email = dados['results'][0]['email']
pais = dados['results'][0]['location']['country']

print("Nome:", nome)
print("Email:", email)
print("País:", pais)
