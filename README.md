# Oyun Kütüphanesi Uygulaması

## Özellikler

- Yeni oyun ekleme
- Oyunlara puan verme
- Oyun silme
- Ortalama puana göre en iyi oyunu önerme
- JSON dosyası ile verilerin saklanması

## Kullanılan Teknolojiler

- Python 3
- PyQt5
- JSON (kalıcı veri saklama)

## Kurulum ve Çalıştırma

1. Gerekli kütüphaneyi yükleyin:

pip install PyQt5

2. Uygulamanın ana dosyasını çalıştırın:

python arayuz.py

## Kullanım

1. Arayüz açıldığında "Oyun Adı", "Tür" ve "Platform" alanlarını doldurarak "Oyun Ekle" butonuna tıklayın.
2. Eklenen oyunlar aşağıdaki koleksiyon listesinde görünecektir.
3. Listedeki bir oyunu seçerek "Seçili Oyunu Sil" butonuyla silebilirsiniz.
4. Bir oyuna puan vermek için önce listeden seçin, ardından sağdaki kutuya 1-10 arasında bir puan girip "Puan Ver" butonuna tıklayın.
5. "En İyi Oyunu Öner" butonuna basarak koleksiyondaki ortalama puanı en yüksek olan oyunu görebilirsiniz.
