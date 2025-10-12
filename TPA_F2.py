b = int(input("b = "))

if not (1 < b < 10):
    print("baza trebuie sa fie intre 1 si 10 exclusiv")


def validitate_xy(nr):
    for cifra in nr:
        if not cifra.isdigit() or int(cifra) >= b:
            return False
    return True


def adunare(nr1, nr2):
    z1 = int(nr1, b)
    z2 = int(nr2, b)
    s = z1 + z2
    return baza_b(s)


def scadere(nr1, nr2):
    z1 = int(nr1, b)
    z2 = int(nr2, b)
    d = z1 - z2
    if d < 0:
        return "rezultat negativ"
    return baza_b(d)


def inmultire(nr1, nr2):
    z1 = int(nr1, b)
    z2 = int(nr2, b)
    p = z1 * z2
    return baza_b(p)


def baza_b(n):
    if n == 0:
        return "0"
    cifre = ""
    while n > 0:
        cifre = str(n % b) + cifre
        n //= b
    return cifre


x = input("primul nr=  ")
y = input("al doilea nr= ")

if validitate_xy(x) and validitate_xy(y):
    print(f"adunare: {adunare(x, y)}")
    print(f"scadere: {scadere(x, y)}")
    print(f"inmultire: {inmultire(x, y)}")
else:
    print("numar scris incorect in baza", b)
