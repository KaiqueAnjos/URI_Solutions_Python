cod, qtd = map(int, input().split(' '))
menu = {1: {'lanche': 'Cachorro Quente', 'preco': 4.00}, 2: {'lanche': 'X-Salada', 'preco': 4.50},
        3: {'lanche': 'X-Bacon', 'preco': 5.00}, 4: {'lanche': 'Torrada Simples', 'preco': 2.00},
        5: {'lanche': 'Refrigerante', 'preco': 1.50}}

total = menu[cod]['preco'] * qtd
print(f'Total: R$ {total:.2f}')