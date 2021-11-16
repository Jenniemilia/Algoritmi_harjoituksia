class Mode:
    def __init__(self):
        self.luvut = {}
        self.korkein = 0
        self.yleisin = None
        self.edellinen = None

    def add(self, x):
        if x not in self.luvut:
            self.luvut[x] = 0
            if self.edellinen is None:
                self.edellinen = x
        self.luvut[x] +=1
        if self.luvut.get(x) == self.korkein and x > self.edellinen:
            return self.edellinen
        elif self.luvut.get(x) == self.korkein and x < self.edellinen:
            self.yleisin = x
            self.edellinen = x
            return x           
        elif self.luvut.get(x) > self.korkein:
            self.korkein = self.luvut[x]
            self.yleisin = x
            self.edellinen = x
            return self.yleisin
        else:
            return self.edellinen
        
                    
if __name__ == "__main__":
    m = Mode()
    print(m.add(3))
    print(m.add(2))
    print(m.add(1))
