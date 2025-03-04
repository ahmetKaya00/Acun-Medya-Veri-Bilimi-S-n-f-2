class Araba:
    """
    marka = "BMW"
    model = "M5"
    yil = 2023

    def bilgi_goster(self):
        print("Bu bir araba sınıfıdır!")
    """

    def __init__(self, marka,model,yil):
        self.marka = marka
        self.model = model
        self.yil = yil
    
    def __del__(self):
        print(f"{self.marka} nesnesi silindi!")

"""
arac = Araba()
print(arac.marka)
arac.bilgi_goster()
"""

arac = Araba("Audi","A4",2022)
del arac
