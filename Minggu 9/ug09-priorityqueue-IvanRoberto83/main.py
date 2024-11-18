class Resto:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def add(self, item, priority):
        self.data.append((priority, item))
        self.data.sort()

    def change_priority(self, item, new_priority):
        if self.is_empty():
            return "Data Kosong"
        else:
            del self.data[0]
            baru = (new_priority,item)
            self.data.append(baru)

    def remove_highest_priority(self):
        ukuran = len(self.data)
        prioritas_tertinggi = self.data[0][0]
       
        for i in range(0,ukuran):
            if self.data[i][0] > prioritas_tertinggi:
                prioritas_tertinggi = self.data[i][0]
        
        for j in range(0,ukuran):
            if self.data[j][0] == prioritas_tertinggi:
                del self.data[j]

    def remove_with_priority(self, priority):
        ukuran = len(self.data)
        for i in range(0,ukuran):
            if self.data[0][i] == priority:
                del self.data[i]

    def display(self):
        for priority, item in self.data:
            print(f"Priority: {priority}, Item: {item}")

antrian = Resto()
antrian.add("Pesan Pizza", 2)
antrian.add("Pesan Ayam Goreng", 1)
antrian.add("Pesan Burger", 3)
print("Isi awal Pesanan:")
antrian.display()

print("\nPesanan Ayam Goreng diminta cepat!!!")
antrian.change_priority("Pesan Ayam Goreng", 4)
antrian.display()

print("\n##### PESANAN PERTAMA SELESAI #####\n")
antrian.remove_highest_priority()

print("Sisa pesanan: ")
antrian.display()

print("\nPesanan dengan prioritas ini telah selesai")
antrian.remove_with_priority(2)
antrian.display()
