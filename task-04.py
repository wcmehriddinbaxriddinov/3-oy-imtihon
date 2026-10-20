talabalar = [("Ali", 85), ("Malika", 95), ("Vali", 78)]

natija = sorted(talabalar, key = lambda t: t[1], reverse = True)

print(f"Natija {natija}")