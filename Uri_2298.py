testes = int(input())
counter = 0
for x in range(testes):
    jogada = [int(x) for x in input().split()]

    pontos = 0
    cartas = {}
    sequencia = True
    count = 0
    carta = 0
    menor = 0

    for x in jogada:
        cartas[x] = jogada.count(x)
    jogada.sort()  
        
    for x in range(1, 5):
        if jogada[x] != jogada[x-1]+1:
            sequencia = False

    for key, value in cartas.items():
        if sequencia == True:
            pontos = 200+jogada[0]
            break
        if value == 4:
            pontos = 180+int(key)
            break
        if (value == 3):
            if (2 in cartas.values()):
                pontos = 160+int(key)
                break
            else:
                pontos = 140+int(key)
                break
        if (value == 2) and (3 not in cartas.values()):
            count += 1
            if int(key) > carta:
                menor = carta
                carta = int(key)
            else:
                menor = int(key)
            if count == 2:
                pontos = carta*3 + menor *2 + 20
                break
            else:
                pontos = carta
    counter += 1
    print(f'Teste {counter}')
    print(pontos)
    print()