def suma_4(a, b, c, d):
    return a + b + c + d

def media_4(i, j, k, m):
    return (i + j + k + m) / 4

def minim_4(a, b, c, d):
    return min(a, b, c, d)

def rad_4(a, b):
    if a == 0:
        return "a nu poate fi 0"
    return -b / a

def cmmicd(n):
    for d in range(2, n + 1):
        if n % d == 0:
            return d

def cmmaredc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def cmmmultipluc(a, b):
    return a * b // cmmaredc(a, b)

def ultima(n):
    return n % 10

def nr_cifre(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

def cifra_sup(n):
    while n >= 10:
        n = n // 10
    return n

x,y,z,q,m = int(input('a= ')), int(input('b= ')), int(input('c= ')), int(input('d= ')), int(input('n= '))

print('a) suma este', suma_4(x,y,z,q))
print('b) media este', media_4(x,y,z,q))
print('e) minimul este', minim_4(x,y,z,q))
print('f) radacina este', rad_4(x,y))
print('g) cel mai mic divizor al lui n este', cmmicd(m))
print('h) cel mai mare divizor comun al nr naturale a b este', cmmaredc(x,y))
print('i) cel mai mic multiplu comun este', cmmmultipluc(x,y))
print('j) ultima cifra in notatia zecimala este', ultima(m))
print('k) nr cifre in notatia zecimala a nr n este', nr_cifre(m))
print('l) cifra superioara in notatia zecimala este', cifra_sup(m))

