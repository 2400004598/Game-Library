class Oyun:
    def __init__(self, ad, tur, platform):
        self.ad = ad
        self.tur = tur
        self.platform = platform
        self.puanlar = []

    def puan_ekle(self, puan):
        self.puanlar.append(puan)

    def ortalama_puan(self):
        if self.puanlar:
            return sum(self.puanlar) / len(self.puanlar)
        return 0