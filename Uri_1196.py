
while True:
    teclado = '`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./'

    try:
        palavra = input()
        tradução = ''
        
        for x in palavra:
            if x == ' ':
                tradução += x
            else:
                tradução += teclado[teclado.index(x)-1]
                
        print(tradução)
    except EOFError:
        break