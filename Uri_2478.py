guia = {}
qtdnomes = int(input())
for x in range(qtdnomes):
    pessoa, pedido1, pedido2, pedido3 = input().split()
    guia[pessoa] = [pedido1, pedido2, pedido3]

while True:
    try:
        nome, presente = input().split()
        if (nome in guia) and (presente in guia[nome]):
            print('Uhul! Seu amigo secreto vai adorar o/')
        else:
            print('Tente Novamente!')
    except EOFError:
        break