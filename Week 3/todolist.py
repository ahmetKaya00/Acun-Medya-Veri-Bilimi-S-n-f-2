def liste_yaz():
    metin = input("yapılacaklar listesine eklemek istediklerin:")
    with open("liste.txt","a",encoding="utf-8") as dosya:
        dosya.write(metin + "\n")
    print("başarılı")

def goruntule():
    with open("liste.txt","r",encoding="utf-8") as dosya:
        print("\nliste notları",dosya.read())

liste_yaz()
goruntule()