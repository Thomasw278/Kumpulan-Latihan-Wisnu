#71230986 - Ivan Roberto Halim

class PriorityQueueSorted:
    def __init__(self):
        self._data = []
        self._size = 0
    
    def is_empty(self):
        if self._size == 0:
            print(True)
        else:
            print(False)
    
    def __len__(self):
        return self._size
    
    def remove(self):
        if self._size == 0:
            print("Data Kosong")
        else:
            del self._data[0]
    
    def peek(self):
        if self._size == 0:
            print("Data Kosong")
        else:
            print(self._data[0])
    
    def mergeSort(self,prioritas):
        if len(prioritas) > 1:
            tengah = len(prioritas) // 2
            sisiKiri = prioritas[:tengah]
            sisiKanan = prioritas[tengah:]
            
            self.mergeSort(sisiKiri)
            self.mergeSort(sisiKanan)
            
            kiri = 0
            kanan = 0
            gabung = 0
            
            while kiri < len(sisiKiri) and kanan < len(sisiKanan):
                if sisiKiri[kiri] >= sisiKanan[kanan]:
                    prioritas[gabung] = sisiKiri[kiri]
                    kiri += 1
                else:
                    prioritas[gabung] = sisiKanan[kanan]
                    kanan += 1
                gabung += 1
            
            while kiri < len(sisiKiri):
                prioritas[gabung] = sisiKiri[kiri]
                kiri += 1
                gabung += 1
            
            while kanan < len(sisiKanan):
                prioritas[gabung] = sisiKanan[kanan]
                kanan += 1
                gabung += 1
    
    def add(self,nama,priority):
        self._data.append((priority,nama))
        self._size += 1
        for i in range(len(self._data)):
            self.mergeSort(self._data)
    
    def print_all(self):
        print(self._data)
    

if __name__ == "__main__":
    myQueue = PriorityQueueSorted()
    myQueue.add('Gian', 2) #
    myQueue.add('Kezia', 8) #
    myQueue.print_all() #
    myQueue.peek() #
    myQueue.add('Glen', 5) #
    myQueue.add('Christo', 9) #
    myQueue.print_all() #
    myQueue.peek() #
    print("========REMOVE========")
    myQueue.remove() #
    myQueue.print_all() #
    myQueue.remove() #
    myQueue.print_all() #
    myQueue.remove() #
    myQueue.print_all() #
    myQueue.add('Saya', 7) #
    myQueue.print_all() #
        