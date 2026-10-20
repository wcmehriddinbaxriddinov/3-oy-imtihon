a = {"olma": 5000, "banan": 12000}
b = {"banan": 15000, "anor": 10000}

natija = {}

for key in a:
    natija[key] = a[key]

for key in b:
    natija[key] = b[key]
    
print(f"Natija: {natija}")
    