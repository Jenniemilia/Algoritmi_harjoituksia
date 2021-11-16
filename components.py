"""Lisää tie kahden kaupungin väliin ja laske montako komponenttia kaupungit muodostavat"""

class Components:
    def __init__(self, n):
        self.n = n
        self.linkki = list(range(self.n+1))
        self.koko = [1] * (n+1)

    def find(self,x):
        while self.linkki[x] != x:
            x = self.linkki[x]
        return x

    def add_road(self,a,b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return 
        if self.koko[a] < self.koko[b]:
            a, b = b, a
        self.koko[a] += self.koko[b]
        self.linkki[b] = a
        

    def count(self):
        setti = set()
        for i in range(1, self.n+1):
            setti.add(self.find(i))
    
        return (len(setti))


if __name__ == "__main__":
    c = Components(5)
    print(c.count()) # 5
    c.add_road(1, 2)
    c.add_road(1, 3)
    print(c.count()) # 3
    c.add_road(2, 3)
    print(c.count()) # 3
    c.add_road(4, 5)
    print(c.count()) # 2v