class Kitap:
    def __init__(self, isim, sayfa):
        self.isim = isim
        self.sayfa = sayfa

    def __str__(self):
        return f"{self.isim}, {self.sayfa} sayfa"
    

kitap = Kitap("Python 101",300)
print(kitap)