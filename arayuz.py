from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QListWidget,
    QLineEdit, QLabel, QFormLayout, QMessageBox, QHBoxLayout
)
from oyuncu import Oyuncu
from oyun import Oyun

class Arayuz(QWidget):
    def __init__(self):
        super().__init__()
        self.oyuncu = Oyuncu("Emre Kenan")
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Oyun Kütüphanesi")
        self.setGeometry(100, 100, 550, 500)
        self.ad_giris = QLineEdit()
        self.tur_giris = QLineEdit()
        self.platform_giris = QLineEdit()
        form_layout = QFormLayout()
        form_layout.addRow("Oyun Adı:", self.ad_giris)
        form_layout.addRow("Tür:", self.tur_giris)
        form_layout.addRow("Platform:", self.platform_giris)
        self.liste = QListWidget()
        self.buton_ekle = QPushButton("Oyun Ekle")
        self.buton_ekle.clicked.connect(self.oyun_ekle)
        self.buton_sil = QPushButton("Seçili Oyunu Sil")
        self.buton_sil.clicked.connect(self.oyun_sil)
        self.puan_giris = QLineEdit()
        self.puan_giris.setPlaceholderText("1 ile 10 arası")
        self.buton_puanla = QPushButton("Puan Ver")
        self.buton_puanla.clicked.connect(self.puan_ver)
        puan_layout = QHBoxLayout()
        puan_layout.addWidget(self.puan_giris)
        puan_layout.addWidget(self.buton_puanla)
        self.buton_oneri = QPushButton("En İyi Oyunu Öner")
        self.buton_oneri.clicked.connect(self.oneri_goster)
        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(self.buton_ekle)
        layout.addWidget(QLabel(" Koleksiyon:"))
        layout.addWidget(self.liste)
        layout.addWidget(self.buton_sil)
        layout.addLayout(puan_layout)
        layout.addWidget(self.buton_oneri)
        self.setLayout(layout)
        self.koleksiyonu_goster()

    def koleksiyonu_goster(self):
        self.liste.clear()
        for oyun in self.oyuncu.koleksiyon.oyunlar:
            puan = oyun.ortalama_puan()
            self.liste.addItem(f"{oyun.ad} ({oyun.tur}, {oyun.platform}) - ⭐ {puan:.1f}")

    def oyun_ekle(self):
        ad = self.ad_giris.text()
        tur = self.tur_giris.text()
        platform = self.platform_giris.text()
        if not ad or not tur or not platform:
            QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun!")
            return
        oyun = Oyun(ad, tur, platform)
        self.oyuncu.koleksiyon.oyun_ekle(oyun)
        self.koleksiyonu_goster()
        self.ad_giris.clear()
        self.tur_giris.clear()
        self.platform_giris.clear()
        self.oyuncu.veriyi_kaydet()

    def oyun_sil(self):
        secili_index = self.liste.currentRow()
        if secili_index >= 0:
            del self.oyuncu.koleksiyon.oyunlar[secili_index]
            self.koleksiyonu_goster()
            self.oyuncu.veriyi_kaydet()

    def puan_ver(self):
        secili_index = self.liste.currentRow()
        puan_str = self.puan_giris.text()
        if secili_index < 0 or not puan_str:
            QMessageBox.warning(self, "Hata", "Lütfen bir oyun seçin ve geçerli puan girin!")
            return
        try:
            puan = int(puan_str)
            if puan < 1 or puan > 10:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Hata", "Puan 1 ile 10 arasında olmalı!")
            return
        oyun = self.oyuncu.koleksiyon.oyunlar[secili_index]
        oyun.puan_ekle(puan)
        self.koleksiyonu_goster()
        self.oyuncu.veriyi_kaydet()
        self.puan_giris.clear()

    def oneri_goster(self):
        en_iyi = self.oyuncu.koleksiyon.en_iyi_oyun()
        if en_iyi:
            QMessageBox.information(
                self, "Oyun Önerisi",
                f"En iyi oyun: {en_iyi.ad} ({en_iyi.tur}, {en_iyi.platform})\n"
                f"Ortalama Puan: ⭐ {en_iyi.ortalama_puan():.1f}"
            )
        else:
            QMessageBox.information(self, "Bilgi", "Henüz önerilecek bir oyun yok.")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    pencere = Arayuz()
    pencere.show()
    sys.exit(app.exec_())