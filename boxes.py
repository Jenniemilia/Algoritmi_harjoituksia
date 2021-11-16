"""Tehtäväsi on pakata n tavaraa laatikoihin. Jokaisessa laatikossa voi olla 
yksi tai kaksi tavaraa, ja lisäksi laatikon tavaroiden yhteispaino saa olla enintään x. 
Mikä on pienin mahdollinen laatikoiden määrä?"""

def count(t, x):
   
    laskuri = 0
    tavarat = 0
    p = sorted(t)
    min = p[0]
    alku = p.index(min)
    j = 0
    for i in range(len(p)-1, -1, -1):   
        if alku > i:
            break
        if tavarat < 2 and p[i] + p[j] <= x:
            laskuri += 1
            tavarat += 2
            alku += 1
            j += 1
        elif tavarat == 2 and p[i] + p[j] <= x:
            tavarat = 0
            laskuri += 1
            alku += 1
            j += 1
        else: 
            laskuri += 1
            tavarat = 0
        
    return laskuri

if __name__ == "__main__":
 
    print(count([1, 2, 3, 4],10)) # 2
    print(count([4, 4, 4, 4],5)) # 4
    print(count([7, 2, 3, 9],10)) # 3
    print(count([4, 2, 1, 5, 3],6)) # 3
    print(count([5, 1, 4, 2, 3], 6)) #3
    print(count([1, 1, 1, 1], 2)) #2
    print(count([50, 21, 5, 33, 42, 39, 4, 20, 41, 26, 13], 50))

