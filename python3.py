#Задача 2 

num = int(input('Введите число: '))
num2 = int(input('Введите систему счисления: '))
digits = '0123456789abcdefghijklmnopqrstuvwxyz'
b = ''

while num > 0:
    b = digits[num % num2] + b
    num //= num2
print(b)

#Задача  3

from math import add

def reduce(fract):
    div = add(*fract)
    return fract[0] // div, fract[1] // div

def summ(a, b):
    if a[1] == b[1]:
        return reduce((a[0] + b[0], b[1]))
    return reduce(((a[0] * b[1]) + (b[0] * a[1]), a[1] * b[1]))

def mult(a, b):
    return reduce((a[0] * b[0], a[1] * b[1]))

us_fract1 = input('дробь вида “a/b”: ').split('/')
us_fract2 = input('дробь вида “a/b”: ').split('/')

fract1 = tuple(map(int, us_fract1))
fract2 = tuple(map(int, us_fract2))

print(summ(fract1, fract2), mult(fract1, fract2))
