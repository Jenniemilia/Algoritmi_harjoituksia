# Lisää annetut kurssit ja niiden esitietovaatimukset. 
# Tulosta kurssit niiden suoritusjärjestyksessä esitietovaatimusten mukaisesti.
# Jos tapaa ei ole, palauta None

class CoursePlan:
    def __init__(self):
        self.kurssit = {}
        self.v = len(self.kurssit)

    def add_course(self,course):
        self.kurssit[course] = []

    def add_requisite(self,course1,course2):
        self.kurssit[course1].append(course2)

    def find(self):
        
        self.jarjestys = []
        self.kayty = {u : "valkoinen" for u in self.kurssit}
        self.onkoSykli = False
        for i in self.kurssit:
            if self.kayty[i] == "valkoinen":
                self.syvyyshaku(i)
        
        if self.onkoSykli == True:
            return None
        
        self.jarjestys.reverse()
        return self.jarjestys

    def syvyyshaku(self, v):
        self.kayty[v] = "harmaa"
        for i in self.kurssit[v]:
            if self.kayty[i] == "harmaa":
                self.onkoSykli = True
                return
            if self.kayty[i] == "valkoinen":
                self.syvyyshaku(i)
        self.kayty[v] = "musta"
        self.jarjestys.append(v)
        
if __name__ == "__main__":
    c = CoursePlan()
    c.add_course("Ohpe")
    c.add_course("Ohja")
    c.add_course("Tira")
    c.add_course("Jym")
    c.add_requisite("Ohpe","Ohja")
    c.add_requisite("Ohja","Tira")
    c.add_requisite("Jym","Tira")
    print(c.find()) # [Ohpe,Jym,Ohja,Tira]
    c.add_requisite("Tira","Tira")
    print(c.find()) # None