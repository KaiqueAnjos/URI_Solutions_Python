val = float(input())
val += 0.001
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for ced in notas:
    qtd = val // ced
    print("{} nota(s) de R$ {}.00".format(int(qtd), ced))
    val -= qtd * ced
print("MOEDAS:")
for cent in moedas:
    qtd = val // cent
    print("{} moeda(s) de R$ {:.2f}".format(int(qtd), cent))
    val -= qtd * cent

