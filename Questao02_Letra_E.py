def medida(a, b, c, d, e, f):
    return a, b, c, d, e, f

def main():
    a = float(input('Qual o valor da altura(m): '))
    c = float(input('Qual o valor do comprimento(m): '))
    l = float(input('Qual o valor da largura(m): '))
    A_piso = l * c
    V_sala = l * c * a
    A_sala = 2 * a * l + 2 * a * c 
    print(f'A área do piso da sala e de {A_piso:.2f} m²')
    print(f'O volume da sala e de {V_sala:.2f} m³')
    print(f'Área das paredes da sala e de {A_sala:.2f} m²')

if __name__=='__main__':
    main()
