"""Pisin alijono, jossa jokaisen kahden vierekkäisen luvun ero on tasan 1"""

def find(t):
    n = len(t)
    # pohjustus
    pisin = [1] *n
    tulos = 1
    for i in range(0, n):
        for j in range (0, i):
            if ((t[j]-1) == t[i]) or ((t[j]+1) == t[i]):
               
                pisin[i] = max(pisin[i], pisin[j] +1)
                
                if tulos < pisin[i]:
                    tulos = pisin[i]   
    return (tulos)

if __name__ == "__main__":
    print(find([1, 2, 3, 4, 5])) # 5
    print(find([5, 5, 5, 5, 5])) # 1
    print(find([5, 2, 3, 8, 2, 4, 1])) # 4