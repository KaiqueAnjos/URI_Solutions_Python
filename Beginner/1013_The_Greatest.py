a, b, c = map(int, input().split(' '))
maior = (a + b + abs(a - b)) / 2
maior = (c + maior + abs(maior - c)) / 2
print(f'{int(maior)} eh o maior')
