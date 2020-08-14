def data(dia, mes, ano):
    return dia, mes, ano

dia = int(input())
mes = int(input())
ano = int(input())
day = data(dia,mes,ano)
print(f'{dia}{mes}{ano}')
