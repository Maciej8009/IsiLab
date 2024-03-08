import random

def podajLiczbe():
    liczba = input("Podaj liczbe: ")
    if liczba.isdigit():
        return int(liczba)
    else:
        print("Podaj liczbę!")
        return podajLiczbe()


liczba = random.randint(1, 100)
liczbaProb = 1

while True:
    liczbaUzytkowanika = podajLiczbe()
    if liczbaUzytkowanika == liczba:
        print("Gratulacja wygrałeś! Wylosowana liczba: ", liczba, "! Zgadłeś za ", liczbaProb, " razem!")
        break
    elif liczbaUzytkowanika > liczba:
        print("Za dużo!")
    else:
        print("Za mało!")
    liczbaProb += 1

