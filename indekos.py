from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, kaplistrik):
        super().__init__("Indekos", kaplistrik)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.kaplistrik = kaplistrik

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni
    def get_summary(self):
        return "Hunian Indekos " + ", kapasitas listrik "+str(self.kaplistrik) + " VA"