class Koleksiyon:
    def __init__(self):
        self.oyunlar = []

    def oyun_ekle(self, oyun):
        self.oyunlar.append(oyun)

    def en_iyi_oyun(self):
        if not self.oyunlar:
            return None
        return max(self.oyunlar, key=lambda o: o.ortalama_puan())
