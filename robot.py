def count(s):
    paikat = {} #x, y
    
   
    paikat[0,0] = 1
    x = 0
    y = 0
    sijainti = (x, y)

    laskuri = 1
     
    for i in s:
        if i == "L":
            x = x-1
            y = y
            sijainti = (x, y)
            if sijainti not in paikat:
                paikat[sijainti] = 1 
                laskuri += 1
                              
        if i == "R":
            x = x+1
            y = y
            sijainti = (x, y)
            if sijainti not in paikat:
                paikat[sijainti] = 1
                laskuri += 1
        if i == "D":
            x = x
            y = y-1
            sijainti = (x, y)
            if sijainti not in paikat:
                paikat[sijainti] = 1
                laskuri += 1
        if i == "U":
            x = x
            y = y+1
            sijainti = (x, y)
            if sijainti not in paikat:
                paikat[sijainti] = 1
                laskuri += 1
    return laskuri
        

print(count("LL")) # 3
print(count("UUDLRR")) # 5
print(count("UDUDUDU")) # 2