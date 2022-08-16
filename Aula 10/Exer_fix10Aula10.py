import numpy as np
lista = []

for x in range(5):
    n = int(input("Digite um  numero:"))
    lista.append(n)
    lista = sorted(lista)

vetor = np.array(lista)
i = vetor(0)
m = len(lista)
print(f"O tamanho do segmento crescente:{m}")
print(f"O primeiro elemento do segmento: {i}")