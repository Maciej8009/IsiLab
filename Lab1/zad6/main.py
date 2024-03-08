def potega(num1):
    return num1 ** 3


num = input("Podaj liczbe: ")
if num.isdigit():
    print(potega(int(num)))
else:
    print("Tylko liczbe można podnieść do potęgi!")
