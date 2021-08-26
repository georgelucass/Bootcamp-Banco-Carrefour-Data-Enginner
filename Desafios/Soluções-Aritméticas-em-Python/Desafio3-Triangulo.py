# A construção desse desafio segue os padrões da DIO para verificar se o código responde corretamente a uma determinada
## entrada e sua saída, por essa razão o código não é tão limpo quanto poderia ser.

a = [float(x) for x in input("Insira os valores dando espaço. (Ex: 6 4 2): ").split()]
if a[0] + a[1] > a[2] and a[0] + a[2] > a[1] and a[1] + a[2] > a[0]:
    print(f"Perimetro = {sum(a):.1f}")
else:
    print(f"Area = {((a[0] + a[1]) * a[2]) / 2:.1f}")