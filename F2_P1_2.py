import math

a,b,c,d=int(input('a=')), int(input('b=')), int(input('c=')), int(input('d=')) 
 
toate_p=[] 
toate_a=[] 
 
def tr_abc(): 
    global a,b,c 
    return a+b>c and b+c>a and a+c>b 
 
def tr_abd(): 
    global a,b,d 
    return a+b>d and b+d>a and a+d>b 
 
def tr_acd(): 
    global a,c,d 
    return a+c>d and d+c>a and a+d>c 
 
def tr_bcd(): 
    global b,c,d 
    return b+c>d and c+d>b and b+d>c 
 
def perimetru(): 
    global a,b,c,d 
    if tr_abc: 
        toate_p.append((a+b+c)) 
    if tr_abd: 
        toate_p.append((a+b+d)) 
    if tr_acd: 
        toate_p.append((a+c+d)) 
    if tr_abc(): 
        toate_p.append((b+c+d)) 
    return toate_p 
 
def aria(): 
    global a,b,c,d 
    if tr_abc(): 
        p=(a+b+c)/2 
        toate_a.append(math.sqrt((p) * (p-a) * (p-b) * (p-c)))     
    if tr_abd(): 
        semiperimetru=(a+b+d)/2 
        toate_a.append(math.sqrt((p) * (p-a) * (p-b) * (p-d))) 
    if tr_acd(): 
        semiperimetru=(a+c+d)/2 
        toate_a.append(math.sqrt((p) * (p-a) * (p-c) * (p-d))) 
    if tr_bcd(): 
        semiperimetru=(b+c+d)/2 
        toate_a.append(math.sqrt((p) * (p-b) * (p-c) * (p-d)))   
    return toate_a 
 
print(f'perimetrele posibile sunt {perimetru()}') 
print(f'ariile posibile sunt {aria()}')