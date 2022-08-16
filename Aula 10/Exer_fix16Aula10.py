import numpy as np

# TRANSFORMAR EM LISTA
listaA = []
listaB = []
listaC = []

# LEITURA DOS VALORES DE A E B
for i in range(10):
    n1 = int(input("Digite um numero para A:"))
    listaA.append(n1)

for i in range(10):
    n2 = int(input("Digite um numero para B:"))
    listaB.append(n2)

# TRANSFORMAR EM VETOR 
vetorA = np.array(listaA)
vetorB = np.array(listaB)
vetorC = np.array(listaC)

# FAZENDO A SUBTRAÇÃO ENTRE OS VETORES A E B
vetorC = vetorA - vetorB
print(vetorC)


