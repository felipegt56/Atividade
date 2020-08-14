def segundos (a, b, c, d, e):
    return a, b, c, d, e

def main():
    h = int(input('Digite a quantidade de horas? '))
    m = int(input('Digite a quantidade de minutos? '))
    s = int(input('Digite a quantidade de segundos? '))
    conversao_horas = h + (m/60) + (s/3600)
    conversao_segundos = conversao_horas *3600
    print(f'Se passaram {conversao_segundos:.0f} segundos desde a última meia-noite.')

if __name__== '__main__':
    main()




        
    
