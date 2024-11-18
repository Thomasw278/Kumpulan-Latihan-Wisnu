class Node:
    def __init__(self, data, priority, next=None):
        self._data = data
        self._priority = priority
        self._next = next
    

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
        else:
            self._tail._next = baru
            self._tail = baru
        self._size += 1
    
    def remove(self):
        if self.isEmpty():
            print("Data Kosong !")
        else:
            if self._size == 1:
                bantu = self._head
                self._head = None
                self._tail = None
                del bantu
            else:
                min_priority = self._head._priority
                hapus = self._head
                while hapus != None:
                    if hapus._priority < min_priority:
                        min_priority = hapus._priority
                    hapus = hapus._next

                hapus = self._head
                while hapus._priority != min_priority:
                    hapus = hapus._next
                
                if hapus == self._head:
                    self._head = self._head._next
                    del hapus
                else:
                    bantu = self._head
                    while bantu._next != hapus:
                        bantu = bantu._next
                    bantu._next = hapus._next
                    del hapus
                    self._tail = self._head
                    
                    while self._tail._next != None:
                        self._tail = self._tail._next
            self._size -= 1
        
    def peek(self):
        if self.isEmpty():
            print("Data Kosong !")
        else:
            if self._size == 1:
                print(tuple([self._head._data, self._head._priority]))
            else:
                min_priority = self._head._priority
                bantu = self._head
                while bantu != None:
                    if bantu._priority < min_priority:
                        min_priority = bantu._priority
                    bantu = bantu._next

                bantu = self._head
                while bantu._priority != min_priority:
                    bantu = bantu._next
                print(tuple([bantu._data,bantu._priority]))


if __name__ == "__main__":
    queue = PriorityQueue()
    queue.printAll()
    queue.addData(10,1)
    queue.addData(20,3)
    queue.addData(23,2)
    queue.addData(21,1)
    queue.addData(24,7)
    queue.addData(29,10)
    queue.printAll()
    print("==========================")
    queue.remove()
    queue.remove()
    queue.printAll()
    queue.peek()