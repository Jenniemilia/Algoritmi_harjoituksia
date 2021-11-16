import time

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, node):
        #node.next = None
        if self.last:
            self.last.next = node
            self.last = node
        else:
            # lista oli tyhja
            self.first = node
            self.last = node

    def delete(self, node):
        if self.first != None:
            if self.first == self.last:
                self.last = None
            self.first = self.first.next

startTime = time.time()
t = LinkedList()
n = 10**5
for i in range(n):
    t.insert(Node(i))

finishTime = time.time()

print(finishTime - startTime)

for i in range(n):
    t.delete(Node(i))

deleteTime = time.time()
print(deleteTime - finishTime)


