class BankaHesabi:
    def __init__(self,bakiye):
        self.__bakiye = bakiye
    
    def bakiye_goster(self):
        print(f"Bakiyeniz: {self.__bakiye} TL")


hesap = BankaHesabi(1000)
hesap.bakiye_goster()
