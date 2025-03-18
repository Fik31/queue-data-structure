try:
    class Queue:
        def __init__(self,n=30):
            self.size = n
            self.current_size = 0
            self.data = []
        
        def isFull(self):
            if self.current_size == self.size:
                return True
            else:
                return False
            
        def isEmpty(self):
            if self.current_size == 0:
                return True
            else:
                return False
            
        def enqueue(self,n):
            if self.isFull():
                print("Maaf antrian sudah penuh")
            else:
                self.data.append(n)
                self.current_size = len(self.data)
                print("Antrian dengan nama ",n,"telah berhasil ditambahkan")
            print("Tekan [Enter] untuk melanjutkan")
            input()
            self.menu()
            
        def dequeue(self):
            if self.isEmpty():
                print("Maaf antrian masih kosong")
                return None
            else:
                datakeluar = self.data.pop(0)
                self.current_size = len(self.data)
                print("-------------------------")
                print("Antrian dengan nama :",datakeluar)
                print("Mohon untuk mengambil barang")
                print("-------------------------")
                print("Antrian setelah ini adalah :",self.data)
            print("Tekan [Enter] untuk melanjutkan")
            input()
            self.menu()
        
        def view(self):
            if self.isEmpty():
                print("Maaf antrian masih kosong")
            else:
                print("=========== DAFTAR ANTRIAN ==========")
                X = 1
                for i in self.data:
                    print(" "+str(X)+". ",i)
                    X +=1
                print("Total Antrian :", len(self.data))
            print("Tekan [Enter] untuk melanjutkan")
            input()
            self.menu()
            
        def Exit(self):
            import sys
            sys.exit()
            
        def menu(self):
            import os
            os.system("CLS")
            print("===========================")
            print("|     PROGRAM ANTRIAN     |")
            print("|------ Daftar Menu ------|")
            print("|1. Tambah Antrian        |")
            print("|2. Panggil Antrian       |")
            print("|3. Lihat Daftar Antrian  |")
            print("|4. Exit                  |")
            print("===========================")
            
            pil = int(input("Masukan no menu yang ingin dipilih: "))
            
            if pil == 1:
                data = input("Masukkan daftar nama antrian : ")
                self.enqueue(data)
            elif pil == 2:
                self.dequeue()
            elif pil == 3:
                self.view()
            elif pil == 4:
                self.Exit
            else:
                print("Maaf pilihan yang anda ketikan tidak ada, silahkan ulangi kembali")
                print("Tekan [Enter] untuk kembali ke menu")
                input()
                self.menu
    q = Queue()
    q.menu()
except ValueError:
    print("Pilihan hanya berupa angka")
    print("Silahkan mulai kembali program!")