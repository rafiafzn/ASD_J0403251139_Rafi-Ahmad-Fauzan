#==============================================================
# Nama   : Rafi Ahmad Fauzan    
# NIM    : J0403251139
# Kelas  : A|P2
#==============================================================

#==============================================================
# Implementasi Dasar : Stack 
#==============================================================

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)
        
#stack ada operasi push(memasukkan head baru) dan pop(menghapus head)
class Stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atas (awalnya kosong)
    
    def push(self, data): #memasukkan data baru pada stack
        #1 Membuat node baru
        nodebaru = Node(data) #instansiasi/memanggil konstruktor pada class Node
        
        #2 node baru menunjuk ke top yang lama (head lama)
        nodebaru.next = self.top
        
        #3 geser top pindah ke node baru
        self.top = nodebaru
    
    def is_empty(self):
        return self.top is None #stack kosong jika top=none
    
    def pop(self): #mengambil/menghapus node paling atas(top/head)
        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None
        
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel(peek)
        self.top = self.top.next #geser top ke node berikutnya
        return data_terhapus

    def peek(self):
        if self.isEmpty():
            print("Stack kosong, tidak bisa peek")
            return None
        return self.top.data #mengembalikan data pada top tanpa menghapusnya

        
    def tampilkan(self):
        #Top -> A -> B -> C -> None
        current = self.top
        print("Top ->", end=" ")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")
    
#instansiasi class stack
s=Stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
s.pop()
print("Peek(lihat top):", s.peek())
s.tampilkan()
print ("Peek(lihat top) :", s.pop()) 
        