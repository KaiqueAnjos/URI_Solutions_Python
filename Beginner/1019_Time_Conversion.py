time = int(input())
seconds = time % 60
minutes = (time // 60) % 60
hours = (time // 60) // 60

print(f'{hours}:', end='')
print(f'{minutes}:', end='')
print(f'{seconds}')
