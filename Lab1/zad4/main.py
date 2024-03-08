licznik = 0

for num in range(200):
    if num % 3 == 0 & num % 4 == 0:
        licznik += 1
        print(num)
print("Liczba liczb podzielnych przez 3 i 4: ", licznik)

