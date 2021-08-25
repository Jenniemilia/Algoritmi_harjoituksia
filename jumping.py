#Laske monellako tavalla voit päästä tasolta 0 tasolle n käyttämällä a tai b hyppyjä?

muisti = {}
def count(n, a, b): 
    #pohjustus 
    laskuri = [0 for i in range(0, n+1)]

    laskuri[0] =  1
    laskuri[a] = a

    
    for i in range(a, n+1):
        
        laskuri[i]= laskuri[i-a]+ laskuri[i-b]
     
    return laskuri[n]

if __name__ == "__main__":
    print(count(4,1,2)) # 5
    print(count(10,2,5)) # 2
    print(count(10,6,7)) # 0
    print(count(3, 1, 3)) # 2
    print(count(30, 3, 5))  # 58
    print(count(50, 2, 3))  # 525456