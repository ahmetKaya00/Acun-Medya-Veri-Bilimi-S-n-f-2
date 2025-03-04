class Kedi:
    def ses_cikar(self):
        return "Miyav!"

class Kopek:
    def ses_cikar(self):
        return "Hav!"
    
hayvanlar = [Kedi(), Kopek()]
for hayvan in hayvanlar:
    print(hayvan.ses_cikar())

    