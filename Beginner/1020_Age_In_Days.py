days = int(input())
years = days // 365
months = (days - 365 * years) // 30
days = (days - 365 * years) % 30
print(f'{years} ano(s)\n'
      f'{months} mes(es)\n'
      f'{days} dia(s)')
