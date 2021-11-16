"""Sinulla on n kolikkoa ja jokaisella kolikolla on jokin kokonaislukuarvo. 
Tehtäväsi on laskea, montako eri summaa voit muodostaa käyttämällä kolikoita"""

def count(t):
    n = len(t)
    if len(t) == 0:
        return 0
    # yläraja, yhteissumma
    s = sum(t)
    summa = 0
    
    #taulukko mahdollisille ja mahdottomille summille
    count = [False for x in range(s * 2)]
    count[0] = True
    for i in range(n):
        for j in range((s)-1, -1, -1):
            if count[j]:
                count[j+t[i]] = True
    for i in range(s):
        if count[i]:
            summa += 1
    return summa

if __name__ == "__main__":
    print(count([3, 4, 5])) # 7
    print(count([1, 1, 2])) # 4
    print(count([2, 2, 2, 3, 3, 3])) # 13
    print(count([42, 5, 5, 100, 1, 3, 3, 7])) # 91