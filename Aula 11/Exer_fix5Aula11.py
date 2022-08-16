
# FUNCAO PARA RETORNAR A TABUADA
listatabuada = []
def tabuada(a):
    x = 1
    while x <= 10:
        n = a* x
        listatabuada.append(n)
        x += 1
    return listatabuada

# OBTENÇÃO DO NUMERO E A CHAMADA E RETORNO DA TABUADA
numero = int(input("Digite um numero para mostrar a tabuada dele:"))
resp = tabuada(numero)
print(f"O valor correspondente a base decimal: {resp}")