import math

a,b,c= float(input('a=')),float(input('b=')),float(input('c='))



def MEDIANA_a():
    global a
    global b
    global c
    if ((a>0) and (b>0) and (c>0) and (a+b>c) and(a+c>b) and (b+c>a)):
        return round((0,5*math.sqrt(2*(b**2) +2*(c**2)-(a**2))),2)
    else:
        return print('Numerele introduse nu satisfac conditia')

def MEDIANA_b():
    global a
    global b
    global c
    if ((a>0) and (b>0) and (c>0) and (a+b>c) and(a+c>b) and (b+c>a)):
        return round((0,5*math.sqrt(2*(a**2) +2*(c**2)-(b**2))),2)

def MEDIANA_c():
    global a
    global b
    global c
    if ((a>0) and (b>0) and (c>0) and (a+b>c) and(a+c>b) and (b+c>a)):
        return round((0,5*math.sqrt(2*(b**2) +2*(a**2)-(c**2))),2)

print('Mediana laturei a=', MEDIANA_a())
print('Mediana laturei b=', MEDIANA_b())
print('Mediana laturei c=', MEDIANA_c())