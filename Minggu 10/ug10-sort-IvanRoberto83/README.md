[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/xkJ1-PbN)
# UG10_Merge-Sort

Buatlah sebuah file python berisi Class PriorityQueueSorted. Fungsi yang harus ada adalah:

  a. is_empty() => melihat apakah Queue kosong atau tidak

  b. __len__()  => return panjang Queue

  c. remove()   => Menghapus data paling depan

  d. peek()     => Mengambil data paling depan

  e. add()      => Menambah isi Queue, cara pengurutan data menggunakan MERGE SORT dan diurutkan dari angka prioritas terbesar ke terkecil (misal: 1,4,3,6 => jadi 6,4,3,1)

  f. print_all => return isi dari Queue urut dari yang terbesar


### TEST CASE

myQueue = PriorityQueueSorted()

myQueue.add('Gian', 2)

myQueue.add('Kezia', 8)

myQueue.print_all()

myQueue.peek()

myQueue.add('Glen', 5)

myQueue.add('Christo', 9)

myQueue.print_all()

myQueue.peek()

print("========REMOVE========")

myQueue.remove()

myQueue.print_all()

myQueue.remove()

myQueue.print_all()

myQueue.remove()

myQueue.print_all()

myQueue.add('Saya', 7)

myQueue.print_all()
