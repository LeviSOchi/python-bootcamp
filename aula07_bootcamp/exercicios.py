# revisão de funções

# 1. Calcular Média de Valores em uma Lista
from typing import List

def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)

levi = calcular_media([10,10,10,10,10])

print(levi)

