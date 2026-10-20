def tashqi(son):
    def ichki(kopaytiruvchi):
        return kopaytiruvchi * son
    return ichki

kopaytiruvchi = int(input("Ko'paytiruvchini kiriting: "))
son = int(input("Kopaytiriladigan sonni kiritng: "))

natija = tashqi(son)(kopaytiruvchi)

print(f"Naitja {natija}")