""""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20/100

valor_desconto = round(preco_original * porcentagem_desconto, 2)
preco_final = round(preco_original - valor_desconto, 2)

print("Produto:", nome_produto)
print("Preço original: R$", preco_original)
print("Desconto: R$", valor_desconto)
print("Preço final: R$", preco_final)
