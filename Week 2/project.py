ogrenciler = []

def ogrenci_ekle():
    ad =input("Öğrenci Adını Girin:")
    soyad =input("Öğrenci Soyadını Girin:")
    yas =int(input("Öğrenci Soyadını Girin:"))
    dersler =input("Öğrencinin aldığı dersleri aralarına virgül koyarak yazın").split(",")

    ogrenci = {
        "Ad": ad,
        "Soyad": soyad,
        "Yaş": yas,
        "Dersler":[ders.strip() for ders in dersler]
    }
    ogrenciler.append(ogrenci)
    print(f"{ad} {soyad} başarıyla eklendi!")


def menu():
        while True:
            print("\nÖğrenci Yönetim Sistemine Hoşgeldiniz!")
            print("1 - Öğrenci Ekle")
            print("6 - Çıkış")

            secim = input("Lütfen yapmak istediğiniz işlemi 1-6 arasında bir değer giriniz.")

            if secim == "1":
                ogrenci_ekle()
            elif secim == "6":
                print("Programdan çıkılıyor......")
                break
            else:
                print("Geçersiz bir tuşlama yaptınız. lütfen 1-6 arasında bir değer girin")

menu()
