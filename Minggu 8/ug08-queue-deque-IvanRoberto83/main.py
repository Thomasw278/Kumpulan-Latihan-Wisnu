class Queue :
    def __init__(self):
        self.data = []
    
    def enqueue(self, data) :
        self.data.append(data)

    def dequeue(self):
        if len(self.data) == 0:
            return
        else :
            return self.data.pop(0)

    def front(self):
        if len(self.data) == 0 :
            return 
        else :
            return self.data[0]
    
    def get_length(self) :
        return len(self.data)

    def write_all_data(self):
        print("DATA: ")
        for i, data in enumerate(self.data):
            print(f"{data}")



# Haram untuk menggunakan list
def get_min(queue):
    dataTerkecil = queue.front()

    for x in range(queue.get_length()):
        if dataTerkecil < queue.front():
            elemen = queue.dequeue()
            queue.enqueue(elemen)
        else:
            dataTerkecil = queue.front()
            elemen = queue.dequeue()
            queue.enqueue(elemen)

    return dataTerkecil
        
def pop(queue):
    dataTerakhir = queue.get_length()
    
    for x in range(dataTerakhir):
        if x == dataTerakhir-1:
            hapus = queue.dequeue()
            return hapus
        else:
            hapus = queue.dequeue()
            queue.enqueue(hapus)
    

if __name__ == "__main__":
    q : Queue = Queue()
    for i in [10, 8, 5, 60,1,2,3,4,100]:
        q.enqueue(i)
    print("==========")
    print("Data Awal")
    q.write_all_data()
    print("==========")
    print(f"Data terkecil = {get_min(q)}")
    print("==========")
    print()
    print("Pembuktian isi queue tidak berubah")
    print("==========")
    print("Data Akhir")
    q.write_all_data()
    print("==========")
    print()
    print("============")
    print("Percobaan Pop")
    print(f"pop - 1 = {pop(q)}")
    print(f"pop - 2 = {pop(q)}")
    print(f"pop - 3 = {pop(q)}")
    print("=============")
    print("Hasil Akhir: ")
    q.write_all_data()
    print("=============")
