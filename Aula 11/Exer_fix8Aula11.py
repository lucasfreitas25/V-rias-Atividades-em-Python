import numpy as np

listaId = []
listanotas = []
# FUNÇÃO PARA LEITURA DOS DADOS DOS ALUNOS
def LerDados():
    id = int(input("Digite o id do aluno:"))
    for i in range(4):
        n = int(input(f"Digite sua nota {i}:"))
        listanotas.append(n)
    nf = float(input("Digite a nota final:"))
    listaId.append(id)
    listanotas.append(nf)

# CALCULO DA MEDIA DE CADA ALUNO
def CalcularMedia(x):
    soma = 0
    for i in range(4):
        if x[i] > x.min():
            soma += x[i]
    soma += x[4]
    return soma

# FUNÇÃO DE EXIBIÇÃO DOS DADOS DOS ALUNOS
def ExibeResultados(y,z):
    print(f"Seu id:{y}")
    print(f"Media final do aluno:{z}")
    if z >= 90 and z <= 100:
        print(f"Seu conceito foi A")
    elif z >= 80 and z <= 89:
        print(f"Seu conceito foi B")
    elif z >= 70 and z <= 79:
        print(f"Seu conceito foi C")
    elif z >= 60 and z <= 69:
        print(f"Seu conceito foi D")
    elif z >= 40 and z <= 59:
        print(f"Seu conceito foi F")
    elif z >= 0 and z <= 39:
        print(f"Seu conceito foi E")
    else:
        print("Invalido")
    
#PROGRAMA PRINCIPAL 
parar = True
while parar == True:
    LerDados()
    VetorId = np.array(listaId)
    VetorNotas = np.array(listanotas)
    media = CalcularMedia(VetorNotas)
    ExibeResultados(VetorId,media)
    resp = input("DESEJA CONTINUAR[S/N]?:").upper()[0]
    if resp == "S":
        listaId.clear()
        listanotas.clear()
        for i in range(1):
            VetorId = 0
        for i in range(4):
            VetorNotas = 0
    if resp == "N":
        parar = False
        

