def kisi_ekle():
    ad = input("Kişinin adını girin: ")
    telefon = input("Kişinin telefon numarasını girin: ")
    with open("rehber.txt","a",encoding="utf-8") as dosya:
        dosya.write(f"{ad}: {telefon}\n")
    print("Kişi başarılı bir şekilde kaydedildi!")

def rehber_goruntule():
    with open("rehber.txt","r",encoding="utf-8") as dosya:
        print("Telefon Rehberi:\n" + dosya.read())
        
rehber_goruntule()


