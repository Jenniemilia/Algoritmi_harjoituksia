"""Tee luokka, jonka avulla pystyy lisäämään kaaren suuntaamattomaan verkkoon 
sekä selvittämään, kuinka pitkä on pisin sellainen polku, jossa jokaisen 
solmun tunnus on suurempi kuin edellisen solmun tunnus."""

class LongPath:
    def __init__(self, n):
        self.n = n
        self.kartta = [[]for _ in range(n+1)]

    def add_edge(self, a, b):
        if a < b:
            self.kartta[a].append(b)
        else:
            self.kartta[b].append(a)

    def calculate(self):
        self.pituus = [0]*(self.n +1)
        self.kayty = [False]* (self.n+1)
        for v in range(1,self.n+1):
            if not self.kayty[v]:
                self.syvyyshaku(v)
        self.tulos= 0
        for i in range(1, self.n+1):
            self.tulos = max(self.tulos, self.pituus[i])
        return self.tulos
    
    def syvyyshaku(self, u):
        self.kayty[u] = True
        for v in range(0,len(self.kartta[u])):
            if not self.kayty[self.kartta[u][v]]:
                self.syvyyshaku(self.kartta[u][v])
            self.pituus[u] = max(self.pituus[u], 1+ self.pituus[self.kartta[u][v]])
           
if __name__ == "__main__":
    l = LongPath(4)
    l.add_edge(1, 2)
    l.add_edge(1, 3)
    l.add_edge(2, 4)
    l.add_edge(3, 4)
    print(l.calculate()) # 2
    l.add_edge(3, 2)
    print(l.calculate()) # 3
