from datetime import date

# Função que obtem numero de dias entre 2 datas
def QuantosDias(date1, date2):
    return (date2-date1).days

# OBTENÇÃO DAS DATAS E RETORNO DA FUNÇÃO
dia1 = int(input("Digite um dia:"))
mes1 = int(input("Digite um mes:"))
ano1 = int(input("Digite um ano:"))
dias2 = int(input("Digite segundo dia:"))
mes2 = int(input("Digite segundo dia:"))
ano2 = int(input("Digite segundo dia:"))     
date1 = date(ano1, mes1, dia1)
date2 = date(ano2, mes2, dias2)
print(QuantosDias(date1, date2), "dias")
