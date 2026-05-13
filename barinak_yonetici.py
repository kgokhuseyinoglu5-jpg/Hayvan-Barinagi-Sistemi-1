# barinak_yonetici.py
import json
import os
from hayvan import Kedi, Kopek

class BarinakYonetici:
    def __init__(self, dosya_adi="veri.json"):
        self.dosya_adi = dosya_adi
        self.hayvanlar = []
        self.verileri_yukle()

    def verileri_yukle(self):
        # Program açıldığında JSON'dan verileri çeker
        if os.path.exists(self.dosya_adi):
            with open(self.dosya_adi, "r", encoding="utf-8") as dosya:
                self.hayvanlar = json.load(dosya)

    def verileri_kaydet(self):
        # Yapılan değişiklikleri JSON dosyasına yazar
        with open(self.dosya_adi, "w", encoding="utf-8") as dosya:
            json.dump(self.hayvanlar, dosya, ensure_ascii=False, indent=4)

    def hayvan_ekle(self, hayvan_nesnesi):
        self.hayvanlar.append(hayvan_nesnesi.sozluge_cevir())
        self.verileri_kaydet()
        print(f"{hayvan_nesnesi.ad} barınağa eklendi!")

    def listele(self):
        print("\n--- Barınaktaki Hayvanlar ---")
        if not self.hayvanlar:
            print("Barınak şu an boş.")
            return
            
        for h in self.hayvanlar:
            print(f"ID: {h['id']} | Tür: {h['tur']} | Ad: {h['ad']} | Durum: {h['durum']} | Sağlık: {h['saglik']}")

    def sahiplendir(self, h_id):
        # ID'si eşleşen hayvanın durumunu günceller
        for h in self.hayvanlar:
            if h["id"] == h_id:
                h["durum"] = "Sahiplendirildi"
                self.verileri_kaydet()
                print(f"Tebrikler! {h['ad']} sahiplendirildi.")
                return
        print("Bu ID'ye ait hayvan bulunamadı.")