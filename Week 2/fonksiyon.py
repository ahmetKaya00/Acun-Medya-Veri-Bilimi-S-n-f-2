def merhaba():
    print("Merhaba, Dünya!")

merhaba()

def selam_ver():
    print("Merhaba!")

selam_ver()

def selam_ver(isim="Misafir"):
    print(f"Selam, {isim}")

selam_ver()

def toplama(a,b):
    print(f"Sonuç: {a + b}")

toplama(3,5)

def kare_al(a):
    return a ** 2
print(kare_al(5))

def topla(*sayilar):
    return sum(sayilar)

print(topla(1,2,3,4,5,6,7,8,9))

def bilgiler(**kwargs):
    for anahtar, deger in kwargs.items():
        print(f"{anahtar}: {deger}")

bilgiler(ad="Ali",yas=25, sehir="Mersin")

kare_alalim = lambda x: x**2
print(kare_alalim(5))

def faktoriyel(n):
    if n == 1:
        return 1
    return n * faktoriyel(n-1)
print(faktoriyel(4))



