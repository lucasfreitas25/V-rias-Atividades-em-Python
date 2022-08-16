n = int(input("Digite um numero para testar se e primo:"))
quant = 0
for i in range(2,n):
    if(n % i == 0):
        quant += 1

if(quant == 0):
    print(f"O numero {n} e primo")
else:
     print(f"O numero {n} nao e primo")
