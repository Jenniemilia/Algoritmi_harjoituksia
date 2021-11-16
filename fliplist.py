from collections import deque

class FlipList:
    def __init__(self):
        self.lista = deque()
        self.kaanteinen = deque()

    def push_last(self,x):
        self.lista.append(x)
        self.kaanteinen.appendleft(x)       

    def push_first(self,x):
        self.lista.appendleft(x)
        self.kaanteinen.append(x)

    def pop_last(self):
        poistettu = self.lista.pop()
        self.kaanteinen.popleft()
        return poistettu

    def pop_first(self):
        poistettu_2 = self.lista.popleft()
        self.kaanteinen.pop()
        return poistettu_2

    def flip(self):
        t = self.lista
        self.lista = self.kaanteinen
        self.kaanteinen = t

if __name__ == "__main__":
    f = FlipList()
    f.push_last(1)
    f.push_last(5)
    f.push_last(3)
    f.flip()
    print(f.pop_last())
    print(f.pop_last())
    print(f.pop_last())
    