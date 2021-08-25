# Yhdistä kaupingit toisiinsa. Mikä on pienin kustannus, jolla voidaan 
# rakentaa tieverkosto niin, että jokaisen kahden kaupungin välillä on reitti?
# -1 jos ei ole mahdollista yhdistää kaikkia kaupunkeja

class NewRoads:
    def __init__(self,n):
        self.n = n
        self.kaaret = []
        self.puu = []
        

    def find(self, x):
        while self.linkki[x] != x:
            x = self.linkki[x]
        return x
    
    def union(self,a,b):
        
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return 
        if self.koko[a] < self.koko[b]:
            a, b = b, a
        
        self.koko[a] += self.koko[b]
        self.linkki[b] = a
       
    def add_road(self,a,b,x):
        self.kaaret.append([a, b, x])
    
    def count(self):
        return self.tulos
            
    def min_cost(self):
        
        #järjestä kaarilista
        self.kaarilista =  sorted(self.kaaret, key = lambda x: x[2])
        self.tulos = self.n
        summa = 0
        self.linkki = list(range(self.n+1))
        self.koko = [1]*(self.n+1)
        for a, b, x in self.kaarilista:
            
            if self.find(a) != self.find(b):
                self.union(a,b)
                self.tulos -= 1
                summa += x
        if self.tulos > 1:
            return -1
   
        else:       
            return summa
        
if __name__ == "__main__":
    n = NewRoads(4)
    n.add_road(1,2,2)
    n.add_road(1,3,5)
    print(n.min_cost()) # -1
    n.add_road(3,4,4)
    print(n.min_cost()) # 11
    n.add_road(2,3,1)
    print(n.min_cost()) # 7
