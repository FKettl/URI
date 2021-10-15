idas = int(input())

for x in range(idas):
    feira = {}
    comprado = 0

    tabela = int(input())
    for x in range(tabela):
        fruta, preço = input().split()
        preço = float(preço)
        feira[fruta] = preço

    compras = int(input())
    for x in range(compras):
        fruta, qtd = input().split()
        qtd = int(qtd)
        if fruta in feira.keys():
            comprado += feira[fruta]*qtd

    print(f'R$ {comprado:.2f}')