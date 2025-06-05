from scipy.constants import precision
import numpy as np

def func(x, *coeffs):#Вычисление обычной функции
    ans = 0
    for i, cf in enumerate(coeffs):
        power = (len(coeffs) - 1 - i)
        ans += cf * x ** power
    return ans


def prime(x, *coeffs):#Вычисление производной
    ans = 0
    for i, cf in enumerate(coeffs):
        power = (len(coeffs) - 1 - i)
        ans += cf * power * x ** (power-1)
    return ans

def newt(limits, precision, *coeffs): #Метод ньютона(касательных)
    precision /= 10
    x = limits[0] #Начальное приближение
    for i in range(1000):
        x_n = x - func(x, *coeffs) / prime(x, *coeffs)
        if abs(x_n-x) < precision:
            return x_n
        x = x_n
    return None

def sol(limits, precision, *coeffs):
    print(newt(limits, precision, *coeffs))

if __name__ == '__main__':
    sol([-5, 5], 0.0001, 1, 0, 0,0)
