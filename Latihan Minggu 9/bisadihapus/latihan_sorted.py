class Node:
    def __init__(self, data, priority, next=None, prev=None):
        self._data = data
        self._priority = priority
        self._next = next
        self._prev = prev
    

class PriorityQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False
    
    def __len__(self):
        return self._size
    
    def printAll(self):
        if self.isEmpty():
            print("Data Kosong !")
        else:
            helper = self._head
            while helper != None:
                print(f"Data {helper._data}, priority : {helper._priority}")
                helper = helper._next
    
    def addData(self,data,priority):
        baru = Node(data,priority)
        if self.isEmpty():
            self._head = baru
            self._tail = baru
        elif self._size == 1:
            if self._head._priority > priority:
                baru._next = self._head
                self._head._prev = baru
                self._head = baru
            else:
                self._head._next = baru
                baru._prev = self._head
                self._tail = baru
        else:
            if self._head._priority > priority:
                baru._next = self._head
                self._head._prev = baru
                self._head = baru
            elif self._tail._priority <= priority:
                self._tail._next = baru
                baru._prev = self._tail
                self._tail = baru
                self._tail._next = None
            else:
                bantu = self._head
                while bantu._priority < priority:
                    bantu = bantu._next
                bantu2 = bantu._prev
                baru._next = bantu
                bantu._prev = baru
                bantu2._next = baru
                baru._prev = bantu2
        self._size += 1
    
    def remove(self):
        if self.isEmpty():
            print("Data Kosong !")
        else:
            hapus = self._head
            if self._size == 1:
                self._head = None
            else:
                self._head = self._head._next
                self._head._prev = None
                del hapus
            self._size -= 1
        
    def peek(self):
        if self.isEmpty():
            print("Data Kosong !")
        else:
            print(tuple([self._head._data, self._head._priority]))


if __name__ == "__main__":
    queue = PriorityQueue()
    queue.printAll()
    queue.addData("Amber",5)
    queue.addData("Diluc",1)
    queue.addData("Beidou",3)
    queue.addData("Kaeya",4)
    queue.printAll()
    print("==========================")
    queue.peek()
    queue.remove()
    queue.remove()
    queue.printAll()
    queue.peek()