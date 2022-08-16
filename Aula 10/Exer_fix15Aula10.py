import numpy as np

lista = []
quant = 0
for i in range(8):
    n = int(input("Digite um numero:"))
    lista.append(n)

vetor_n = np.array(lista)

x = int(input("Digite um valor para verificar seu multiplos no vetor:"))
for i in range(8):
    if(vetor_n[i] % x == 0):
        quant += 1

print(f"A quantidade de multiplos de x:{quant}")