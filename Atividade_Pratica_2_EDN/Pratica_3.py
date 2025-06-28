"""
3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
"""

nota_1 = round(7.5, 2)
nota_2 = round(8.0, 2)
nota_3 = round(6.5, 2)

media = round ((nota_1 + nota_2 + nota_3) / 3, 2)

print ("Nota 1:", nota_1)
print("Nota 2:", nota_2)
print("Nota 3:", nota_3)
print ("Media final do aluno:", media)

