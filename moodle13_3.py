from random import randint
import time

class Components:
    def __init__(self,n):
        self.n = n
        self.vanhempi = list(range(self.n+1))
        self.koko = [1] * (n+1)
        self.tulos = n

    def find(self,x):
        while self.vanhempi[x] != x:
            x = self.vanhempi[x]
        return x

    def union(self, a,b):
        a = self.find(a)
        b = self.find(b)
        
        if self.koko[a] < self.koko[b]:
            a, b = b, a
        self.koko[a] += self.koko[b]
        self.vanhempi[b] = a
    
    def add_road(self,a,b):
        if self.find(a) != self.find(b):
             
            self.union(a,b)
            self.tulos -= 1

    def count(self):
        return self.tulos

if __name__ == "__main__":
    alkuaika = time.time()
    n = 100000
    c = Components(n)
    for i in range(n):
        a = randint(1,n)
        b = randint(1,n)
        c.add_road(a,b)
    
    loppuaika = time.time()
    print(c.count())
    print(loppuaika-alkuaika)
    