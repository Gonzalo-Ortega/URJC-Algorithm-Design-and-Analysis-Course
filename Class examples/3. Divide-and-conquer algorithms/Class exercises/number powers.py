# Divide and conquer powers

def power(x, n):
    if n == 0:
        result = 1
    elif n == 1:
        result = x
    elif n % 2 == 0:
        aux = power(x, n // 2)
        result = aux * aux
    else:
        result = x * power(x, n - 1)
    return result


def main():
    print('Cálcullo de x ** n por divide y vencerás')
    x = float(input('Valor de x:', ))
    n = int(input('Valor de n: '))
    print('x ** n', power(x, n))
