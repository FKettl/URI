while True:
    try:
        hora, minuto = [int(x) for x in input().split(':')]
        horabin = ['', '', '', '']
        minbin = ['', '', '', '', '', '']
        for x in range(1, 5):
            if hora % 2 == 0:
                horabin[4-x] = ' '
            elif hora % 2 == 1:
                horabin[4-x] = 'o'
            hora = hora // 2

        for x in range(1, 7):
            if minuto % 2 == 0:
                minbin[6-x] = ' '
            elif minuto % 2 == 1:
                minbin[6-x] = 'o'
            minuto = minuto // 2

        print(' ____________________________________________')
        print('|                                            |')
        print('|    ____________________________________    |_')
        print('|   |                                    |   |_)')
        print('|   |   8         4         2         1  |   |')
        print('|   |                                    |   |')
        print(f'|   |   {horabin[0]}         {horabin[1]}         {horabin[2]}         {horabin[3]}  |   |')
        print('|   |                                    |   |')
        print('|   |                                    |   |')
        print(f'|   |   {minbin[0]}     {minbin[1]}     {minbin[2]}     {minbin[3]}     {minbin[4]}     {minbin[5]}  |   |')
        print('|   |                                    |   |')
        print('|   |   32    16    8     4     2     1  |   |_')
        print('|   |____________________________________|   |_)')
        print('|                                            |')
        print('|____________________________________________|')
        print()

    except EOFError:
        break

