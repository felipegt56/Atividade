def data(dia, mes, ano):
    return dia, mes, ano

dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))
day = data(dia,mes,ano)
print(f'{dia}/{mes}/{ano}')
