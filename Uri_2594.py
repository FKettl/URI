# -*- coding: utf-8 -*-

n = int(input())

for x in range(n):
    indexes = []
    texto = input().split()
    palavra = input()
    conta = 0
    

    for x in texto:
        if x == palavra:
            indexes.append(conta)
        conta += len(x) + 1

    if indexes == []:
        print('-1')
    else:
        for x in range(len(indexes)):
            if x < (len(indexes)-1):
                print(f'{indexes[x]} ', end='')
            else:
                print(f'{indexes[x]}')
        
