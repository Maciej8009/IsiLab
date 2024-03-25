import sqlite3


conn = sqlite3.connect('Uczelnie.db')

print("1. Wszystkich studentów")
query1 = conn.execute('SELECT * FROM Student')
for row in query1:
    print(row)

print("Wszystkich studentów 1 grupy")
query2 = conn.execute('SELECT * FROM Student WHERE GrupaID=1')
for row in query2:
    print(row)

print("Studentów którzy z jednego przedmiotu otrzymali ocenę wyższą bądź równą 4.")
query3 = conn.execute('SELECT * FROM Student WHERE StudentID in (SELECT StudentID FROM ocena WHERE ocena>=4) GROUP BY StudentID')
for row in query3:
    print(row)

print("Wszystkich wykładowców z prowadzonymi przez nich przedmiotami")
query4 = conn.execute('SELECT Imie, Nazwisko, Przedmiot_Nazwa FROM Wykładowca, Przedmiot WHERE Wykładowca.WykładowcaID=Przedmiot.WykładowcaID')
for row in query4:
    print(row)

print("Wyświetlić wydział z wszystkimi jego grupami studenckimi")
query5 = conn.execute('SELECT Wydział_nazwa, GrupaNazwa FROM Wydział, Grupa_studencka WHERE Grupa_studencka.WydziałID = Wydział.WydziałID ')
for row in query5:
    print(row)

print("Wszystkich studentów wraz z średnią arytmetyczną ich ocen.")
query6 = conn.execute('SELECT Student.StudentID, Student.Imie, Student.Nazwisko, AVG(Ocena.Ocena) FROM Student, Ocena WHERE Student.StudentID=Ocena.StudentID GROUP BY Student.StudentID')
for row in query6:
    print(row)

conn.close()