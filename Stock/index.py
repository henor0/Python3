class StokManager:
    def __init__(self):
        # fjalor me pjesët dhe sasitë e tyre
        self.stok = {}

    def shto_pjese(self, kodi, emri, sasia_fillestare=0):
        if kodi in self.stok:
            print(f"Pjesa {kodi} ekziston tashmë.")
        else:
            self.stok[kodi] = {'emri': emri, 'sasia': sasia_fillestare}
            print(f"Pjesa {emri} me kod {kodi} u shtua me sasi fillestare {sasia_fillestare}.")

    def hyrje(self, kodi, sasia):
        if kodi in self.stok:
            self.stok[kodi]['sasia'] += sasia
            print(f"Hyrje: {sasia} të {self.stok[kodi]['emri']} shtuar në stok.")
        else:
            print("Kjo pjesë nuk ekziston në stok.")

    def dalje(self, kodi, sasia):
        if kodi in self.stok:
            if self.stok[kodi]['sasia'] >= sasia:
                self.stok[kodi]['sasia'] -= sasia
                print(f"Dalje: {sasia} të {self.stok[kodi]['emri']} u hoqën nga stoku.")
            else:
                print(f"Nuk ka mjaftueshëm sasi në stok. Aktualisht: {self.stok[kodi]['sasia']}.")
        else:
            print("Kjo pjesë nuk ekziston në stok.")

    def shfaq_stokun(self):
        print("\nStoku aktual:")
        for kodi, info in self.stok.items():
            print(f"{kodi}: {info['emri']} - Sasia: {info['sasia']}")

# Shembull përdorimi:
manager = StokManager()
manager.shto_pjese('P001', 'Pjese A', 10)
manager.shto_pjese('P002', 'Pjese B', 5)

manager.hyrje('P001', 5)
manager.dalje('P002', 3)
manager.dalje('P001', 20)  # gabim, sasia nuk mjafton

manager.shfaq_stokun()
