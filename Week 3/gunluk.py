def gunluk_yaz():
    not_metni = input("Günlüğünüze eklemek istediğiniz notu yazın: ")
    with open("gunluk.txt","a",encoding="utf-8") as dosya:
        dosya.write(not_metni + "\n")
    print("Not başarılı bir şekilde kaydedildi!")



def gunluk_goruntule():
    with open("gunluk.txt","r",encoding="utf-8") as dosya:
        print("\nGünlük Notları:\n " + dosya.read())


gunluk_goruntule()