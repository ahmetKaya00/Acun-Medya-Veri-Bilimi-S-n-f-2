#Aritmetiksel Operatörler

sayi1 = 10
sayi2 = 3

print("Toplam: ", sayi1 + sayi2)
print("Çıkar: ", sayi1 - sayi2)
print("Çarp: ", sayi1 * sayi2)
print("Böl: ", sayi1 / sayi2)
print("Böl: ", sayi1 // sayi2)
print("Üs: ", sayi1 ** sayi2)
print("Mod: ", sayi1 % sayi2)

#Karşılaştırma Operatörleri

print(sayi1 < sayi2)
print(sayi1 == sayi2)
print(sayi1 != sayi2)

#Mantıksal Operatörler
yas = 18
ehliyet = True

print(yas >= 18 and ehliyet)
print(yas < 18 or ehliyet)
print(not ehliyet)

#Koşullu İfadeler

sayi = int(input("Bir sayı girin: "))

if sayi > 0:
    print ("SAyı Pozitiftir.")
elif sayi < 0:
    print("SAyi Negatiftir.")
else:
    print("Sayı sıfırdır.")