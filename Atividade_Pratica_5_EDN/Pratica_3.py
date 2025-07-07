"""
Exercicio 3: Crie uma função que verifique se uma palavra ou frase é um palindromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda "Sim", se o resultado for False, responda "Não".
"""

import string

def eh_palindromo(texto):
    texto = texto.lower()
    texto = ''.join(char for char in texto if char in string.ascii_lowercase)
    return "Sim" if texto == texto[::-1] else "Não"

frase = input("Digite uma palavra ou frase: ")
print("É palíndromo?", eh_palindromo(frase))
