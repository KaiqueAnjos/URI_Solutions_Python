codProd1, qtdProd1, precoProd1 = input().split(' ')
codProd1 = int(codProd1)
qtdProd1 = int(qtdProd1)
precoProd1 = float(precoProd1)
codProd2, qtdProd2, precoProd2 = input().split(' ')
codProd2 = int(codProd2)
qtdProd2 = int(qtdProd2)
precoProd2 = float(precoProd2)

total = precoProd1 * qtdProd1 + precoProd2 * qtdProd2
print(f'VALOR A PAGAR: R$ {total:.2f}')