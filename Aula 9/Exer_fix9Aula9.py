resp = "S"
soma = 0
x = 0
while(resp == "S"):
    idade = int(input("Digite a idade:"))
    soma += idade
    x += 1
    resp = input("Deseja continuar[S/N]:")

media = soma/x
print(f"A media de idade: {media}")