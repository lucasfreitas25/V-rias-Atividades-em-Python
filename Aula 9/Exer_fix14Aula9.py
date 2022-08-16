n = 1
soma = 0
while(n <= 500):
    if(n % 2 != 0 and n % 3 == 0):
        soma += n
        n += 1
    else:
        n += 1

print(soma)