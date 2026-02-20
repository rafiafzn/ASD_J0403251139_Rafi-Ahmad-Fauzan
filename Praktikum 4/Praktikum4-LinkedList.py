#==============================================================
#Nama   : Rafi Ahmad Fauzan
#NIM    : J0403251139
#Kelas  : A|P2
#==============================================================

#==============================================================
#Implementasi Dasar : Node pada linked list
#==============================================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class node dipanggil
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

#1) membuat node dengan instantiasi class node
NodeA = Node("A")
NodeB = Node("B")
NodeC = Node("C")

#2) menghubungkan Node : A -> B -> C -> None
head = NodeA
NodeA.next = NodeB
NodeB.next= NodeC
#4) Traversal: menelusuri node dari head sampai ke none
current=head
while current is not None:
    print(current.data) #menampulkan data pada node saat ini
    current = current.next #pindah ke node berikutnya  