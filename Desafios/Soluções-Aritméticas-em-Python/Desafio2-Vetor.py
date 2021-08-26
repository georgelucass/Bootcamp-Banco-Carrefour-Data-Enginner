# A construção desse desafio segue os padrões da DIO para verificar se o código responde corretamente a uma determinada
## entrada e sua saída, por essa razão o código não é tão limpo quanto poderia ser.

x = int(input())
N = [x]
for i in range (0,10):
        square = x*2
        N.append(square)
        x = square

for v in range (0,10):
    print("N[{}] = {}".format(v, N[v]))