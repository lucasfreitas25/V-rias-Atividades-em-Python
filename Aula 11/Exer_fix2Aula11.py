import numpy as np

# Função que calculo a soma
def soma_maior(a):
    soma = 0
    aux = a.min
    for i in range(4):
        if a[i] > a.min():
            soma += a[i]
    return soma

# CRIAÇÃO E ATRIBUIÇÃO DE VALORES
listanum = []
for i in range(4):
    n = int(input("Digite um numero:"))
    listanum.append(n)

Numeros = np.array(listanum)

# CHAMADA E RETORNO DA SOMA DOS 3 MAIORES NUMEROS
somanum = soma_maior(Numeros)
print(f"A soma entre 3 maiores numeros e de: {somanum}")
