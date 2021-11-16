"""Toteuta luokka, jonka avulla pystyy lisäämään tien kahden kaupungin 
välille sekä muodostamaan taulukon kaupunkien välimatkoista."""

class AllRoutes:
    def __init__(self, n):
        self.n = n
        self.inf = 10**9
        self.taulukko = [[self.inf]*(n) for _ in range(n)]

    def add_road(self, a, b, x):
        if self.taulukko[a-1][b-1] > x:
            self.taulukko[a-1][b-1] = x
        if self.taulukko[b-1][a-1] > x:
            self.taulukko[b-1][a-1] = x
        
    def get_table(self):
                        
        for k in range(self.n):
            self.taulukko[k][k] = 0
            for i in range(self.n):
                for j in range(self.n):
                    self.taulukko[i][j] = min(self.taulukko[i][j], self.taulukko[i][k]+
                    self.taulukko[k][j])
        
        for j in range(len(self.taulukko)):        
            for z in range(len(self.taulukko)):
                if(self.taulukko[j][z] == self.inf):
                    self.taulukko[j][z] = -1       
        return self.taulukko


if __name__ == "__main__":
    a = AllRoutes(5)
    a.add_road(3, 4, 6)
    a.add_road(4, 5, 5)
    a.add_road(4, 5, 6)
    a.add_road(1, 5, 7)
    a.add_road(1, 4, 7)
    a.add_road(4, 5, 1)
    a.add_road(3, 4, 8)
    a.add_road(2, 3, 6)
    a.add_road(4, 5, 4)
    print(a.get_table())
    """[[0, 19, 13, 7, 7], [19, 0, 6, 12, 13], [13, 6, 0, 6, 7], [7, 12, 6, 0, 1], [7, 13, 7, 1, 0]]"""