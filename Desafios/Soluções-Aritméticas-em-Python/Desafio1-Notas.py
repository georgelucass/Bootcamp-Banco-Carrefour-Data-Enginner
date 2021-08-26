# A construção desse desafio segue os padrões da DIO para verificar se o código responde corretamente a uma determinada
## entrada e sua saída, por essa razão o código não é tão limpo quanto poderia ser.

nota = int(input('Insira o valor da nota de 0 a 100: '))

if 0 <= nota < 1:
    print('\nA nota correspondente é: ')
    print('E')
elif 1 <= nota <=35:
    print('\nA nota correspondente é: ')
    print('D')
elif 36 <= nota <= 60:
    print('\nA nota correspondente é: ')
    print('C')
elif 61 <= nota <= 85:
    print('\nA nota correspondente é: ')
    print('B')
elif 86 <= nota <= 100:
    print('\nA nota correspondente é: ')
    print('A')

