def polyndrom(txt):
    return "tak" if txt[::-1] == txt else "nie"


txt = input("Wpisz teks do sprawdzenia: ")
print(polyndrom(txt))


