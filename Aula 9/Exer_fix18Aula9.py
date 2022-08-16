import math

x = False
fim = False
chapa1 = 0
chapa2 = 0
chapa3 = 0
branco = 0
nulo = 0
soma = 1

while(fim == True):
    print("1 para chapa 1")
    print("2 para chapa 2")
    print("3 para chapa 3")
    print("0 para branco")
    print("9 para nulo")
    escolha = int(input("Digite o voto:"))
    if(escolha == 1):
        chapa1 += 1
        soma += 1
    elif(escolha == 2):
        chapa2 += 1
        soma += 1
    elif(escolha == 3):
        chapa3 += 1
        soma += 1
    elif(escolha == 0):
        branco += 1
        soma += 1
    elif(escolha == 9):
        nulo += 1
        soma += 1
    resp = str(input("Deseja continuar:[S/N]"))
    if (resp == "N"):
        fim == True
        
soma -= 1
x = (chapa1/soma)*100
y = (chapa2/soma)*100
z = (chapa3/soma)*100
h = (branco/soma)*100
s = (nulo/soma)*100

if(x > 50):
    print("Chapa 1 eleita")
elif(y > 50):
    print("Chapa 2 eleita")
elif(z > 50):
    print("Chapa 3 eleita")
else:
    print("Vamos para segundo turno")

