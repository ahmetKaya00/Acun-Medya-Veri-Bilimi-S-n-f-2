import json

data = {"ad": "Ahmet", "yaş": 15, "şehir": "İstanbul"}
with open("veri.json","w", encoding="utf-8") as dosya:
    json.dump(data, dosya, ensure_ascii=False, indent=4)

with open("veri.json","r",encoding="utf-8") as dosya:
    data =json.load(dosya)
    print(data)