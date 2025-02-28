with open("ornek.txt","r",encoding="utf-8") as dosya:
    icerik = dosya.read()
    print(icerik)

with open("ornek.txt","w",encoding="utf-8") as dosya:
    dosya.write("Bu üzerine yazılan metin.\n")

with open ("ornek.txt","a",encoding="utf-8") as dosya:
    dosya.write("Bu eklenen metin!\n")