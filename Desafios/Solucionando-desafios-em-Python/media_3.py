# A construção desse desafio segue os padrões da DIO para verificar se o código responde corretamente a uma determinada
## entrada e sua saída, por essa razão o código não é tão limpo quanto poderia ser.

n1, n2, n3, n4= input().split()
n1 = float(n1)*2
n2 = float(n2)*3
n3 = float(n3)*4
n4 = float(n4)*1

media = (n1 + n2 + n3 + n4)/ (2 + 3 + 4 + 1)
print('Media: %.1f' %media)

if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
elif 5<= media <= 6.9:
    print('Aluno em exame.')

    n5 = float(input())
    final = (n5+media)/2

    print('Nota do exame: %.1f' %n5)

    if final >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %.1f' % final)