# Luokka jolla pystyy lisäämään tien kaupunkien välille ja etsimään lyhimmän reitin.
# Ilmoita lyhin reitti tai -1 jos reittiä ei ole.

class BestRoute:
    def __init__(self,n):
        self.n = n
        self.edges = []

    def add_road(self,a,b,x):
        self.edges.append((a,b,x))
        self.edges.append((b,a,x))

    def find_route(self,a,b):
        inf = 10**9
        self.dist = [inf] * (self.n+1)
        self.dist[a] = 0

        while True:
            self.change = False
            for edge in self.edges:
        
                if self.dist[edge[0]] + edge[2] < self.dist[edge[1]]:
                    self.dist[edge[1]] = self.dist[edge[0]] + edge[2]
                    self.change = True
    
            if not self.change:
                break
        if self.dist[b]== inf:
            return -1
        else:
            return self.dist[b]

if __name__ == "__main__":
    b = BestRoute(5)
    print(b.find_route(3,4)) # -1
    b.add_road(3,5,7)
    print(b.find_route(3,4)) #-1
    print(b.find_route(1,4)) #-1
    b.add_road(3,4,6)
    print(b.find_route(4,5)) #13
    b.add_road(4,5,4)
    b.add_road(1,2,7)
    b.add_road(1,3,4)
    print(b.find_route(3,4)) #6