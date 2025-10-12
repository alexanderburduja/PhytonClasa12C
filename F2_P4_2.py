import math 
 
a = float(input("introduceti a: ")) 
b = float(input("introduceti b: ")) 
c = float(input("introduceti c: ")) 

def inaltimi_tr(a, b, c): 
    if ((a>0) and (b>0) and (c>0) and (a+b>c) and(a+c>b) and (b+c>a)): 
        A = aria(a, b, c) 
        laturi = [a, b, c] 
        inaltimi = [] 
        
        for l in laturi: 
            h = 2 * A / l 
            inaltimi.append(h) 
        
        return inaltimi 
    else: 
        return False 

def aria(a, b, c): 
    aria = (a + b + c) / 2 
    A = math.sqrt(aria * (aria - a) * (aria - b) * (aria - c)) 
    return A 
 
 
 
rezultat = inaltimi_tr(a, b, c) 
 
if rezultat is False: 
    print("cele trei numere nu pot forma un triunghi") 
else: 
    print(f"inaltimile sunt hA = {rezultat[0]:.2f}, hB = {rezultat[1]:.2f}, hC = {rezultat[2]:.2f}")