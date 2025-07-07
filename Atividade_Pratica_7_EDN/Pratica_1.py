"""
1 - Leia um arquivo que contém dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de execução constantes.
"""

import re
import statistics

tempos = []

with open("log.txt", "r") as arquivo:
    for linha in arquivo:
        match = re.search(r"Tempo de execução: (\d+\.?\d*)", linha)
        if match:
            tempos.append(float(match.group(1)))

if tempos:
    media = statistics.mean(tempos)
    desvio = statistics.stdev(tempos)
    print("Média:", round(media, 2))
    print("Desvio padrão:", round(desvio, 2))
else:
    print("Nenhum tempo encontrado no arquivo.")
