def media (a, b, c):
    return a, b, c

def main():
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o Segundo  número: '))
    c = int(input('Digite o Terceiro número: '))
    media = (a + b + c)/ 3
    print(f'A média é {media:.1f}')

if __name__== '__main__':
    main()
