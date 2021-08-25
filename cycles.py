#Tehtäväsi on toteuttaa luokka, jonka avulla pystyy lisäämään kaaren suunnattuun verkkoon
# sekä tutkimaan, onko verkossa suunnattua sykliä.

#1= valkoinen
#2= harmaa
#3 = musta


class Cycles:
    def __init__(self,n):
        self.n = n
        self.verkko = [[]for _ in range(n+1)]
         
    def add_edge(self,a,b):
        self.verkko[a].append(b)
  
    def check(self):
        self.onkoSykli = False
        sykli = ["valkoinen"]* (self.n +1)
        #print(self.sykli)
       
        for v in range(1,self.n+1):
            if sykli[v] == "valkoinen":
                self.syvyyshaku(v, sykli)
        return self.onkoSykli
        
    def syvyyshaku(self, u, sykli):
        sykli[u] = "harmaa"
    
        for v in self.verkko[u]:
            if sykli[v]== "harmaa":
                self.onkoSykli = True
                return 
                          
            if sykli[v]== "valkoinen":
                self.syvyyshaku(v, sykli)
           
        sykli[u] = "musta"
        #return False
 
if __name__ == "__main__":
    c = Cycles(5)
    c.add_edge(5,3)
    c.add_edge(5,1)
    c.add_edge(1,4)
    c.add_edge(1,2)
    c.add_edge(1,3)
    print(c.check()) #False
    print(c.check()) #False
    c.add_edge(4,5)
    print(c.check()) # True
    c.add_edge(2,5)