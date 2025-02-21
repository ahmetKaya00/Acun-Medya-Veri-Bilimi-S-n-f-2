meyveler = ["Elma","Armut","Kiraz","Muz"]
print(meyveler)

print(meyveler[0])
print(meyveler[-2])

meyveler[1] = "Karpuz"
print(meyveler)

meyveler.append("Çilek")
print(meyveler)
meyveler.insert(1,"Portakal")
print(meyveler)
meyveler.remove("Muz")
print(meyveler)


demet = ("Elma","Armut","Muz")
print(demet)

#demet[1] = "Karpuz" HATA!!!!
#demet.append("Çilek") HATA!!!!

ogrenci = {
    "ad": "Ali",
    "soyad": "Kaya",
    "yaş": 25
}

print(ogrenci["ad"])

for anahtar, deger in ogrenci.items():
    print(f"{anahtar}: {deger}")

renkler = {"Kırmızı","Mavi","Sarı","Yeşil","Mavi"}
print(renkler)

ogreciler = []

def ogrenci_ekle(ad,soyad,yas,ders):
    ogrenci = {
        "Ad": ad,
        "Soyad": soyad,
        "Yaş": yas,
        "Dersler": ders
    }
    ogreciler.append(ogrenci)
    print(f"Öğrenci Eklendi: {ad} {soyad}")

def ogrenci_listele():
    for ogrenci in ogreciler:
        print(f"{ogrenci['Ad']} {ogrenci['Soyad']} - Yaş: {ogrenci['Yaş']} ")

ogrenci_ekle("Ahmet","Kaya",36,"Veri Bilimi")
ogrenci_ekle("Mehmet","Kaya",36,"Web Geliştirme")

ogrenci_listele()