# hayvan.py

class Hayvan:
    def __init__(self, id_no, ad, yas, saglik_durumu):
        self.id_no = id_no
        self.ad = ad
        self.yas = yas
        self.saglik_durumu = saglik_durumu
        # Kapsülleme (Encapsulation): Durum değişkeni gizlidir (private)
        self.__durum = "Barınakta" 

    # Kapsüllenen veriye erişim metotları (Getter / Setter)
    def durum_getir(self):
        return self.__durum

    def sahiplendir(self):
        self.__durum = "Sahiplendirildi"

    def sozluge_cevir(self):
        # JSON'a kaydetmek için veriyi sözlüğe (dict) çeviriyoruz
        return {
            "id": self.id_no,
            "tur": self.__class__.__name__,
            "ad": self.ad,
            "yas": self.yas,
            "saglik": self.saglik_durumu,
            "durum": self.__durum
        }

# Kalıtım (Inheritance): Kedi sınıfı Hayvan sınıfının özelliklerini miras alır
class Kedi(Hayvan):
    def __init__(self, id_no, ad, yas, saglik_durumu, tuy_rengi):
        super().__init__(id_no, ad, yas, saglik_durumu)
        self.tuy_rengi = tuy_rengi

    def sozluge_cevir(self):
        veri = super().sozluge_cevir()
        veri["ekstra"] = f"Tüy: {self.tuy_rengi}"
        return veri

# Kalıtım (Inheritance)
class Kopek(Hayvan):
    def __init__(self, id_no, ad, yas, saglik_durumu, cinsi):
        super().__init__(id_no, ad, yas, saglik_durumu)
        self.cinsi = cinsi

    def sozluge_cevir(self):
        veri = super().sozluge_cevir()
        veri["ekstra"] = f"Cins: {self.cinsi}"
        return veri