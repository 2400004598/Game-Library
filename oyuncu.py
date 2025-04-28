import json
import os
from koleksiyon import Koleksiyon
from oyun import Oyun

class Oyuncu:
    def __init__(self, isim):
        self.isim = isim
        self.koleksiyon = Koleksiyon()
        self.veri_dosyasi = f"veri/{self.isim}_koleksiyon.json"
        self.veriyi_yukle()

    def favori_ekle(self, oyun):
        self.koleksiyon.oyun_ekle(oyun)

    def veriyi_kaydet(self):
        data = []
        for oyun in self.koleksiyon.oyunlar:
            data.append({
                "ad": oyun.ad,
                "tur": oyun.tur,
                "platform": oyun.platform,
                "puanlar": oyun.puanlar
            })

        with open(self.veri_dosyasi, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def veriyi_yukle(self):
        if os.path.exists(self.veri_dosyasi):
            with open(self.veri_dosyasi, "r", encoding="utf-8") as f:
                oyun_listesi = json.load(f)
                for o in oyun_listesi:
                    oyun = Oyun(o["ad"], o["tur"], o["platform"])
                    oyun.puanlar = o.get("puanlar", [])
                    self.koleksiyon.oyun_ekle(oyun)