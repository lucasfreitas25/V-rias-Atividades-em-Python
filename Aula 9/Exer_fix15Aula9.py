escolha = 0
saldo = 0.0
while(escolha != 4):
    print("------- Banco --------")
    print("1 para consultar saldo")
    print("2 para saque")
    print("3 para deposito")
    print("4 para sair")
    escolha = int(input("Qual opcao vai querer:"))
    if(escolha == 1):
        print(saldo)
    elif(escolha == 2):
        saque = float(input("Qual valor a ser sacado:"))
        saldo -= saque
    elif(escolha == 3):
        deposito = float(input("Digite o valor a ser depositado:"))
        saldo += deposito
    elif(escolha == 4):
        print("Voce saiu")
        break
