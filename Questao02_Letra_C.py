def cubo (a, b):
    return a, b

def main():
    n = int(input('Digite um número pra saber o valor dele ao cubo: '))
    cubo = (n**3)
    print(f'O valor de {n}³ = {cubo:.0f}')
if __name__== '__main__':
    main()
