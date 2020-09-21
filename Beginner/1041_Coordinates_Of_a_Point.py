x, y = map(float, input().split(' '))
if x > 0 < y:
    print('Q1')
elif x < 0 < y:
    print('Q2')
elif x < 0 > y:
    print('Q3')
elif x > 0 > y:
    print('Q4')
elif x == y == 0:
    print('Origem')
elif y == 0 != x:
    print('Eixo X')
elif x == 0 != y:
    print('Eixo Y')