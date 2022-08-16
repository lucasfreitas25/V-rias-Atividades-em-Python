import numpy as np

# TRANSFORMAR EM LISTA
listaA = []
listaB = []
listaU = []
listaI = []

# LEITURA DOS VALORES DE A E B
for i in range(3):
    n1 = int(input("Digite um numero para A:"))
    listaA.append(n1)
    listaU.append(n1)

for i in range(3):
    n2 = int(input("Digite um numero para B:"))
    listaB.append(n2)
    listaU.append(n2)

# TRANSFORMAR EM VETOR 
vetorA = np.array(listaA)
vetorB = np.array(listaB)
vetorU = np.array(listaU)


# VETORES U E I
# Uniao de vetores
print(vetorU)

for i in range(3):
    if vetorA[i] == vetorB[i]:
        listaI.append(vetorA[i])

vetorI = np.array(listaI)
print(vetorI)