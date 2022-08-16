# CRIANDO A MATRIZ
matriz1 = [[0.0 for i in range(4)] for j in range(4)]
matriz2 = [[0.0 for i in range(4)] for j in range(4)]
matrizSoma = [[0.0 for i in range(4)] for j in range(4)]

# ATRIBUINDO VALORES NAS MATRIZES
for i  in range(4):
    for j in range(4):
        matriz1[i][j] = float(input(f"Digite um valor da matriz 1[{i},{j}]:"))

for i  in range(4):
    for j in range(4):
        matriz2[i][j] = float(input(f"Digite um valor da matriz 4[{i},{j}]:"))

for i  in range(4):
    for j in range(4):
        matrizSoma[i][j] = matriz1[i][j] + matriz2[i][j]        

# MOSTRANDO OS VALORES DA MATRIZ SOMA PEDIDA
print("|    MATRIZ SOMA     |")
for i  in range(4):
    for j in range(4):
        print(f"[{matrizSoma[i][j]:^5}]", end='')
    print()


