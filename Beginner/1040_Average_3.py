n1, n2, n3, n4 = map(float, input().split(' '))
media_p = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
print(f'Media: {media_p:.1f}')

if media_p >= 7.0:
    print('Aluno aprovado.')
elif media_p < 5.0:
    print('Aluno reprovado.')
elif 5.0 <= media_p <= 6.9:
    print('Aluno em exame.')
    exam = float(input())
    print(f'Nota do exame: {exam:.1f}')
    media_p = (media_p + exam) / 2

    if media_p >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media_p:.1f}')
