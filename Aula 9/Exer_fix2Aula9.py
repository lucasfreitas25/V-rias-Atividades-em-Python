

lado1 = int(input("Digite o valor do lado 1:"))
lado2 = int(input("Digite o valor do lado 2:"))
lado3 = int(input("Digite o valor do lado 3:"))

x = lado1 + lado2
y = lado1 + lado3
z = lado2 + lado3

if(lado1 < z and lado2 < y and lado3 < x):
    if(lado1 == lado2 and lado1 == lado3 and lado2 == lado3):
        print("Triangulo Equilatero")
    elif(lado1 == lado2 or lado2 == lado3 or lado1 == lado3):
        print("Triangulo Isosceles")
    elif(lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
       print("Triangulo escaleno")


