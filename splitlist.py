def count(t):
    pituus = len(t)
    laskuri = 0

    vasen_puoli = [0]*pituus
    vasen_puoli[0] = t[0]
    edellinen = vasen_puoli[0]
    for i in range(0, pituus):
        if t[i] > edellinen:
            vasen_puoli[i] = t[i]
            edellinen = t[i]
        else:
            vasen_puoli[i] = edellinen

    oikea_puoli = [0]*pituus
    oikea_puoli[pituus-1] = t[pituus-1]
    edellinen_o = oikea_puoli[pituus-1]
    for i in range(pituus-1, -1, -1):
        if t[i] < edellinen_o:
            oikea_puoli[i]= t[i]
            edellinen_o = t[i]
        else:
            oikea_puoli[i] = edellinen_o  
   
    for i in range (0, pituus-1):
        if oikea_puoli[i+1] > vasen_puoli[i]:
            laskuri += 1

    return laskuri
    
if __name__ == "__main__":
    print(count([1,2,3,4,5])) # 4
    print(count([5,4,3,2,1])) # 0
    print(count([2,1,2,5,7,6,9])) # 3
    print(count([5, 6, 6, 7, 8, 10, 3])) #0
    print(count([2, 1, 2, 6, 3, 4, 9, 12])) #3