def media (a, b, c):
    return a, b, c

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    media = (a + b + c)/ 3
    print(f'{media:.1f}')

if __name__== '__main__':
    main()
