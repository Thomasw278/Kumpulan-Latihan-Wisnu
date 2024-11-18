from queue import Queue
from files import Stack

def balikQueue(Q):
    S = Stack()
    str = ""
    n = len(Q)
    for i in range(n):
        str = Q.first()
        S.push(str)
        Q.dequeue()
    while (S.isEmpty()==False):
        Q.enqueue(S.top())
        S.pop()
            
#main program
ipt = Queue()
ipt.enqueue("A")
ipt.enqueue("B")
ipt.enqueue("C")
print(ipt.first())
balikQueue(ipt)
print(ipt.first())