import math
import numpy as np

lista = []*10
# Obtendo os valores
for i in range(10):
    n = float(input("Digite sua altura:"))
    lista.append(n)

# Media
altura = np.array(lista)
print(f"A media das altura: {altura.mean():.2f}")

# Calculo desvio padrao
for i in range(10):
    soma = (altura[i] - altura.mean())**2
    
desvio = math.sqrt(soma/5)
print(f"O desvio padrão: {desvio}")