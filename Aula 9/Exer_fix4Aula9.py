# LENDO OS DADOS
salario = float(input("Digite o salario:"))
vendastotais = int(input("Digite as vendas do mes:"))
salarionovo = salario
#Alterando os salarios
if(vendastotais > 100 and vendastotais <= 500):
    salarionovo += 500
elif(vendastotais > 500 and vendastotais <= 750):
    salarionovo += 750
elif(vendastotais > 750):
    salarionovo += 1000
else:
    print("O salario se manteve sem acrescimo dos premios")

print(salarionovo)