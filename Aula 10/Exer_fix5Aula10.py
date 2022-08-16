import numpy as np
posicao = 0
lista = []*50
listadiminuida = []*50
for i in range(50):
   n = float(input("Digite um valor:"))
   lista.append(n)

numeros = np.array(lista)
print(f"A media:{numeros.mean()}")

for i in range(4):
    x = abs(numeros.mean() - numeros[i])
    listadiminuida.append(x)

diminuida = np.array(listadiminuida)
for i in range(4):
    if(diminuida[i] == diminuida.mean()):
        posicao = i

print(f"O menor valor da lista subtraida da media e a posicao:{diminuida.min()}, {numeros[posicao]}")