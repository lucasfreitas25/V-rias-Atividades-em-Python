
r1 = float(input("Digite o valor da resistencia 1:"))
r2 = float(input("Digite o valor da resistencia 2:"))
r3 = float(input("Digite o valor da resistencia 3:"))
x = input("Digite o circuito e em serie ou paralelo[S/P]:")

if(x == "S"):
    rfinal = r1 + r2 + r3
elif(x == "P"):
    rfinal = 1/(1/r1 + 1/r2 + 1/r3)
else:
    print("Valor invalido")

print(f"O valor total da resistencia: {rfinal}")