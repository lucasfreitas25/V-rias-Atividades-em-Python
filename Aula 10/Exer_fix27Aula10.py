# CRIANDO A MATRIZ
matriz = [[0 for i in range(2)] for j in range(2)]


# ATRIBUINDO VALORES NAS MATRIZES
for i  in range(2):
    for j in range(2):
        matriz[i][j] = float(input(f"Digite um valor da matriz [{i},{j}]:"))

# MOSTRANDO A MATRIZ 
print("|    MATRIZ      |")
for i  in range(2):
    for j in range(2):
        print(f"[{matriz[i][j]:^5}]", end='')
    print()

# MOSTRANDO A MATRIZ TRANSPOSTA
print("|    MATRIZ TRANSPOSTA     |")
for j  in range(2):
    for i in range(2):
        print(f"[{matriz[i][j]:^5}]", end='')
    print()
