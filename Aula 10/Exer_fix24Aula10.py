import numpy as np
ordem = int(input("Digite a ordem da matriz:"))
matriz = [[0.0 for i in range(ordem)] for j in range(ordem)]

listaA = []
listaB = []
listaC = []

for i  in range(ordem):
    for j in range(ordem):
        matriz[i][j] = float(input(f"Digite um valor[{i},{j}]:"))

# ACHANDO OS VALORES ACIMA DA DIAGONAL PRINCIPAL
for i  in range(ordem):
    for j in range(ordem):
        if j > i:
            listaA.append(matriz[i][j])    

# ACHANDO OS VALORES DA DIAGONAL SECUNDARIA
for i  in range(ordem):
    for j in range(ordem):
        if i + j == ordem - 1:
            listaB.append(matriz[i][j])
# ACHANDO OS VALORES ABAIXO DA DIAGONAL PRINCIPAL
for i  in range(ordem):
    for j in range(ordem):
        if i > j:
            listaC.append(matriz[i][j]) 

A = np.array(listaA) 
B = np.array(listaB)
C = np.array(listaC)

print("|Valores acima da Diagonal Principal|")
print(A)

print("|Valores da Diagonal Secundária|")
print(B)

print("|Valores abaixo da Diagonal Principal|")
print(C)