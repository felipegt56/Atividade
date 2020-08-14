def media (a, b, c):
    return a, b, c


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    medi = (a + b + c)/ 3
    med = media(a, b, c)
    print(f'{medi}')
if __name__== '__main__':
    main()
