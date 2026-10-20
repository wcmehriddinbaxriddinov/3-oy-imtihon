import json

with open("products.json", "r") as file:
    mahsulotlar = json.load(file)

nom = input("Mahsulot nomi: ")
miqdor = int(input("Yangi miqdor: "))

topildi = False
for mahsulot in mahsulotlar:
    if mahsulot["nom"] == nom:
        mahsulot["miqdor"] = miqdor
        topildi = True

if topildi:
    with open("products.json", "w") as fayl:
        json.dump(mahsulotlar, fayl, indent=4)
    print("Miqdor yangilandi.")
else:
    print("Mahsulot topilmadi.")