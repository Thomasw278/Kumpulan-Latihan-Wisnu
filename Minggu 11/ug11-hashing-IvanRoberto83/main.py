class Restoran:
    def __init__(self):
        self.size = 5
        self.map = [None] * self.size

    def _getHash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char) # mendapatkan nilai ASCII
        return hash % self.size

    def _probing(self, key):
        for index in range(self.size):
            # probeHash = (self._getHash(key)+index) % self.size
            probeHash = self._linearProbing(key, index)
            # valid bila index adalah None atau ber-flag deleted
            if (self.map[probeHash] is None) or (self.map[probeHash] == 'deleted'):
                return probeHash

    # melakukan linear probing
    def _linearProbing(self, key, index):
        return (self._getHash(key)+index) % self.size

    # menambahkan key pada hash table
    def tambahReservasi(self, key, value):
        keyHash = self._getHash(key)
        keyValue = [key,value]
        
        if self.map[keyHash] is None:
            self.map[keyHash] = list([keyValue])
            return True
        else:
            keyHash = self._probing(key)
            if keyHash is None:
                return False
            
        self.map[keyHash] = list([keyValue])
        return False

    def lihatReservasi(self, key):
        keyHash = self._getHash(key)
        if (self.map[keyHash] != "deleted") and (self.map[keyHash] is not None):
            for index in range(self.size):
                keyHash = self._linearProbing(key,index)
                if self.map[keyHash][0][0] == key:
                    return self.map[keyHash][0][1]
        return "None"

    def reserveDone(self, key):
        keyHash = self._getHash(key)
        if self.map[keyHash] is None:
            return False
        for index in range(self.size):
            keyHash = self._linearProbing(key,index)
            if self.map[keyHash][0][0] == key:
                self.map[keyHash] = "deleted"
                return True
        return False

    def printAll(self):
        print('---List Reservasi----')
        for item in self.map:
            if item is not None:
                print(str(item))

if __name__ == "__main__":
    rak1 = Restoran()

    rak1.tambahReservasi("Draine", "Family Dinner")
    rak1.tambahReservasi("Perry", "Birthday Party")
    rak1.tambahReservasi("Octo", "Romantic Dinner")
    rak1.tambahReservasi("Peter", "Lunch")
    rak1.tambahReservasi("Hrain", "Test Food Wedding")
    rak1.tambahReservasi("Gura", "Garden Party")
    
    print(rak1.lihatReservasi("Octo"))
    print(rak1.lihatReservasi("Buna"))

    rak1.reserveDone("Pery")
    rak1.reserveDone("Draine")
    rak1.printAll()
