mahsulotlar = {"non": 4000, "sut": 12000, "olma": 8000}

nom = input("Mahsulot nomi kiriting: ")
narx = int(input("Yangi narxini kiritng: "))

topildi = False

for key in mahsulotlar:
    if key == nom:
        mahsulotlar[key] = narx
        topildi = True
        
if topildi:
    print("Mahsulot topildi")
    print(f"Yangilangan ro'yxat: {mahsulotlar}")
else:
    print("Mahsulot topilmadi")
      
    