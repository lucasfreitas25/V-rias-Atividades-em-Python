from asyncio.windows_events import NULL
import math

listabhaska = []
# FUNÇÃO QUE CALCULA  O DELTA E BHASKARA
def bhaskara(x,y,z):
    delta = y**2 - 4 * x * z
    if delta < 0:
        bhaska1 = NULL
        bhaska2 = NULL
    elif delta >= 0:
        bhaska1 = (-y + math.sqrt(delta))/(2 * x)
        bhaska2 = (-y - math.sqrt(delta))/(2 * x)
    listabhaska.append(bhaska1)
    listabhaska.append(bhaska2)
    return listabhaska

# OBTENÇÃO DOS VALORES DE A,B,C E O RETORNO DA FUNÇÃO
a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))
resp = bhaskara(a,b,c)
print(f"O(s) valor(s) da raiz(s) é de: {resp}")
