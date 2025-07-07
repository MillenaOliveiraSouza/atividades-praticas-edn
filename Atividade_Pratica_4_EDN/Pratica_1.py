"""
Exercicio 1: Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória. ​
"""

import random
import string

tamanho = int(input("Quantos caracteres você quer na sua senha? "))

caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

print("Senha gerada:", senha)
