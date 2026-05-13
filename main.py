# main.py
from barinak_yonetici import BarinakYonetici
from hayvan import Kedi, Kopek

def menu():
    yonetici = BarinakYonetici()
    
    while True:
        print("\n=== HAYVAN BARINAĞI SİSTEMİ ===")
        print("1. Kedi Ekle")
        print("2. Köpek Ekle")
        print("3. Hayvanları Listele")
        print("4. Hayvan Sahiplendir")
        print("5. Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            id_no = input("ID: ")
            ad = input("Ad: ")
            yas = input("Yaş: ")
            saglik = input("Sağlık Durumu: ")
            tuy = input("Tüy Rengi: ")
            yeni_kedi = Kedi(id_no, ad, yas, saglik, tuy)
            yonetici.hayvan_ekle(yeni_kedi)
            
        elif secim == "2":
            id_no = input("ID: ")
            ad = input("Ad: ")
            yas = input("Yaş: ")
            saglik = input("Sağlık Durumu: ")
            cins = input("Cinsi: ")
            yeni_kopek = Kopek(id_no, ad, yas, saglik, cins)
            yonetici.hayvan_ekle(yeni_kopek)
            
        elif secim == "3":
            yonetici.listele()
            
        elif secim == "4":
            h_id = input("Sahiplendirilecek Hayvanın ID'si: ")
            yonetici.sahiplendir(h_id)
            
        elif secim == "5":
            print("Sistemden çıkılıyor. İyi günler!")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    menu()