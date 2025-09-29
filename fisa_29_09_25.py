import math
x,y = int(input('a= ')), int(input('b= '))
def suma_ab(a,b):
    return x+y

def prod_ab(a,b): 
    return x*y

def media_ab(a,b):
    return (x+y)/2

def min_ab(a,b):
    return min(x,y)

def max_ab(a,b):
    return max(x,y)

def cmmdc_ab(a,b):
    while b!=0:
        r= a%b
        a=b
        b=r
    return a

def cmmmc_ab(a,b):
    return (a*b)// cmmdc_ab(a,b)

def divizori(n):
    n=n if n>=0 else -n
    d=[]
    for i in range(1, n+1):
                   if n%i == 0:
                        d.append(i)
    return d
                   

def div_com_ab(a,b):
    comuni=[]
    for d in divizori(a):
        if d in divizori(b):
            comuni.append(d)
    return comuni

def mul_com_ab(a,b, k=5):
     m=[]
     x=cmmmc_ab(a,b)
     for i in range(1,k+1):
          m.append(x*i)
     return m

def cif_com_ab(a,b):
     a_str= str(a if a>=0 else -a)
     b_str= str(b if b>=0 else -b)
     comune=[]
     for c in a_str:
          for c in b_str and c not in comune:
               comune.append(c)
          return comune    
    
def cif_prima_ab(a,b):
     a_str= str(a if a>=0 else -a)
     b_str= str(b if b>=0 else -b)
     diferite=[]
     for c in a_str:
          for c in a_str:
               if c not in b_str and c not in diferite:
                    diferite.append(c)           
     return diferite 

def prietene(a,b):
     return len(divizori(a)) == len(divizori(b))

print('a) suma numerelor ', suma_ab(x,y))
print('b) produsul numerelor ', prod_ab(x,y))
print('c) media numerelor ', media_ab(x,y))
print('d) cel mai mare divizor comun al numerelor ', cmmdc_ab(x,y))
print('e) cel mai mic multiplu comun al numerelor ', cmmmc_ab(x,y))
print('f) minimul numerelor ', min_ab(x,y))
print('g) maximul numerelor ', max_ab(x,y))
print('h)',x,'+',y, '=', suma_ab(x,y))
print('i)',x,'*',y, '=', prod_ab(x,y))
print('j) divizorii comuni ai numerelor ', div_com_ab(x,y))
print('j) divizorii comuni ai numerelor ', div_com_ab(x,y))
print('l) cifrele care se contin in ambele ', cif_com_ab(x,y))
print('m) cifrele care se contin doar in prima ', cif_prima_ab(x,y))

print('n) sunt prietene', prietene(x,y))

