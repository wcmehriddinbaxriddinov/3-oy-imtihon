import csv

mahsulotlar = [
    ["Olma", 8000, 12],
    ["Non", 4000, 20],
    ["Sut", 14000, 5]
]

with open("products.csv", "w", newline="", encoding="utf-8") as file:
    yozuvchi = csv.writer(file)
    yozuvchi.writerow(["nom", "narx", "soni"])
    yozuvchi.writerows(mahsulotlar)

with open("products.csv", "r") as file:
    viewer = csv.DictReader(file)
    xotira = list(viewer)

for mahsulot in mahsulotlar:
    print(mahsulot)