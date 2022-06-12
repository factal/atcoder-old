s, p = map(int, input().split())

def solv_quadratic_equation(a, b, c):
    D = (b**2 - 4*a*c) ** (1/2)
    x_1 = (-b + D) / (2 * a)
    x_2 = (-b - D) / (2 * a)

    return x_1, x_2

a = 1
b = -1 * s
c = p


x1, x2 = solv_quadratic_equation(float(a) , float(b) , float(c))

if x1.is_integer() and x1 > 0 and x2.is_integer() and x2 > 0:
    print('Yes')
else:
    print('No')