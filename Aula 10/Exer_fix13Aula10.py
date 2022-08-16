import numpy as np

lista = []
lista2 = []
lista3 = []

for i in range(10):
    cliente = str(input("Digite o nome do cliente:"))
    lista.append(cliente)

vetor_cliente = np.array(lista)

for i in range(10):
    loca = int(input("Digite a quantidade de alocacoes de dvds:"))
    lista2.append(loca)

vetor_loca = np.array(lista2)

for i in range(10):
    quant = 0
    if(vetor_loca[i] % 10 == 0):
        quant = vetor_loca/10
        lista3.append(quant)

vetor_gratis = np.array(lista3)
print(vetor_cliente)
print(vetor_gratis)
