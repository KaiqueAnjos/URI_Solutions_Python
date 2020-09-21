num = float(input())
if 0 <= num <= 100:
    intervalos = ([0, 25], [25, 50], [50, 75], [75, 100])
    for i in intervalos:
        if i[0] <= num <= i[1]:
            if i[0] == 0:
                print(f'Intervalo [{i[0]},{i[1]}]')
            else:
                print(f'Intervalo ({i[0]},{i[1]}]')
            break
else:
    print('Fora de intervalo')