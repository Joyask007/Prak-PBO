class Mahasiswa:
    
    def __init__(self,nama,nim,kelas,sks):
        self.nama=nama
        self.nim=nim
        self.kelas=kelas
        self.sks=sks
    
    def data (self):
        print("Nama : ",self.nama)
        print("Nim  : ",self.nim)
        print("Kelas: ",self.kelas)
        print("Sks  : ",self.sks)
    
mhs=Mahasiswa("Joy Aloita Sembiring",12114006119140036,"RB",20)
mhs.data()
