while True:
    posicao = 'N'
    total = 0
    n = int(input())
    if n == 0:
        break
    comandos = input().upper()
    direitas = comandos.count('D')
    esquerdas = comandos.count('E')
    total -= esquerdas
    total += direitas
    if total % 4 == 3:   #Se total % 4 == 0 ele ficaria N mas como N ja é o default do posição não preciso por outro elif
        posicao = 'O'
    elif total % 4 == 2:
        posicao = 'S'
    elif total % 4 == 1: 
        posicao = 'L'     
    print(posicao) 


