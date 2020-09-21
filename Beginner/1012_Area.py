a, b, c = map(float, input().split(' '))

trian = (a * c) / 2
circ = 3.14159 * pow(c, 2)
trap = ((a + b) * c) / 2
quad = pow(b, 2)
retan = a * b

print(f'TRIANGULO: {trian:.3f}\n'
      f'CIRCULO: {circ:.3f}\n'
      f'TRAPEZIO: {trap:.3f}\n'
      f'QUADRADO: {quad:.3f}\n'
      f'RETANGULO: {retan:.3f}')
