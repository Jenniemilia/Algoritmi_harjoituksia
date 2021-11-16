"""Annettuna on lista, jonka jokainen alkio on eri kokonaisluku. Tehtäväsi 
on ilmoittaa listan indeksit järjestyksessä niitä vastaavien alkioiden mukaan 
pienimmästä suurimpaan."""

def get(t):
    uusi_lista = list(enumerate(t, 0))
    uusi_lista.sort(key = lambda x: x[1])    
    return ([x[0] for x in uusi_lista])

if __name__ == "__main__":
    print(get([1, 2, 4, 3])) # [0,1,3,2]
    print(get([4, 2, 1, 3])) # [2,1,3,0]
    print(get([6, 2, 8, 5, 3])) # [1,4,3,0,2]