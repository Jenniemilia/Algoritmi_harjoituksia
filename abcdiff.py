# Toteuta lista, jossa on kaikki n merkin pituiset merkkijonot, joissa 
# jokainen merkki on A, B tai C ja missään kohdassa ei ole vierekkäin kahta 
# samaa merkkiä. Listan tulee olla aakkosjärjestyksessä.

def toinen(tulos, n, string, m, lista):
  
    if m == n:
        mjono = ""
        for j in tulos:
            mjono += j
        lista.append(mjono)
        
    else:
        for i in string:
            if m == 0:
                tulos[m] = i
                toinen(tulos, n, string, m+1, lista)
            if m >= 1 and tulos[m-1] != i:
                tulos[m] = i
                toinen(tulos, n, string, m+1, lista)
                    
    return lista
def create(n):
    string = "ABC"
    tulos = [0]*n
    return (toinen(tulos, n, string, 0, []))  
        
if __name__ == "__main__":
    print(create(1)) # [A,B,C]
    print(create(2))
    print(create(3)) # [AB,AC,BA,BC,CA,CB]
    print(len(create(5))) # 48
 