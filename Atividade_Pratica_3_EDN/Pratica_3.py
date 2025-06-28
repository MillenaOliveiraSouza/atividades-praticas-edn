"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

temperatura = float(input("Digite a temperatura: "))
unidade_de_origem = input("Digite a unidade de origem (Celsius, Fahrenheit ou Kelvin): ").lower()
unidade_desejada = input("Digite a unidade de destino (Celsius, Fahrenheit ou Kelvin): ").lower()

if unidade_de_origem == "celsius":
    if unidade_desejada == "fahrenheit":
        resultado = (temperatura * 9/5) + 32
    elif unidade_desejada == "kelvin":
        resultado = temperatura + 273.15
    else:
        resultado = temperatura

elif unidade_de_origem == "fahrenheit":
    if unidade_desejada == "celsius":
        resultado = (temperatura - 32) * 5/9
    elif unidade_desejada == "kelvin":
        resultado = (temperatura - 32) * 5/9 + 273.15
    else:
        resultado = temperatura

elif unidade_de_origem == "kelvin":
    if unidade_desejada == "celsius":
        resultado = temperatura - 273.15
    elif unidade_desejada == "fahrenheit":
        resultado = (temperatura - 273.15) * 9/5 + 32
    else:
        resultado = temperatura

print("Temperatura convertida:", round(resultado, 2), unidade_desejada.capitalize())
