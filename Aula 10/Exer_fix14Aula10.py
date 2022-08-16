
numeros = {

}
fim = True
for i in range(8):
    n = float(input("Digite um numero:"))
    if n in numeros:
        numeros[n] = numeros[n] + 1
    else:
        numeros[n] = 1

while(fim == True):
    v = float(input("Digite um numero que queria verificar:"))
    print(f"A quantidade de vezes que o numero apareceu foi de:{numeros[v]}")
    resp = str(input("Deseja continuar[S/N]")).upper()[0]
    if(resp == 'N'):
        fim = False