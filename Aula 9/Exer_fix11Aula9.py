A = 90
B = 150
An = A
Bn = B
ano = 0
while(A < B):
    A = A *1.03
    B = B *1.015
    ano += 1

print(f"A quatidade de anos que precisou para A ser maior que B:{ano}")