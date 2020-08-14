def data(dia, mes, ano, variavel):
    return dia, mes, ano, variavel


def main():
    dia = int(input())
    mes = int(input())
    ano = int(input())
    variavel = '/'
    day = data(dia,mes,ano, variavel)
    print(f'{dia}{variavel}{mes}{variavel}{ano}')
if __name__== '__main__':
    main()
