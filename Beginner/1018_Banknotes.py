val = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
print(val)
for ced in notas:
    qtd = val // ced
    print(f'{int(qtd)} nota(s) de R$ {ced},00')
    val -= qtd * ced

