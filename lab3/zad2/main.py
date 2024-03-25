import sqlite3


con = sqlite3.connect("Uczelnie.db")
cur = con.cursor()
cur.execute('INSERT INTO Uczelnia VALUES (1, "AMW", "Daleko")')
cur.execute('INSERT INTO Wydział VALUES (1, "Mechaniczno Elektryczny", 1), (2, "Nauk Humanistycznych i Społecznych", 1)')
cur.execute('INSERT INTO Wykładowca (wykładowcaid, Imie, Nazwisko, wydziałid) VALUES (1, "Mateusz", "Kupiec", 1), (2, "Małgorzata", "Kupiec", 2), (3, "Marcin", "Najman", 1), (4, "Marcin", "Krasucki", 2), (5, "Sebastian", "Alvarez", 2);')
cur.execute('INSERT INTO Przedmiot (przedmiotid, przedmiot_nazwa, wykładowcaid) VALUES (1, "Freestyle z Bonzo", 1), (2, "Gotowanie z Kobrą", 2), (3, "Jak przegrywać każdą walkę", 3), (4, "Łapanie piwa w locie" ,4), (5, "Jak radzić sobie z dwubiegunowością", 5);')
cur.execute('INSERT INTO Grupa_studencka (grupaid, grupanazwa, wydziałid) VALUES (1, "Alkofizycy", 1), (2, "Alkohumany", 2);')
cur.execute('INSERT INTO Student (studentid, imie, nazwisko, grupaid) VALUES (1, "Janusz", "Stachecki", 1), (2, "Rozalia", "Kossowska", 1), (3, "Hanna", "Kurz", 1), (4, "Marzena", "Juszczak", 2), (5, "Kazimierz", "Perkowski", 2), (6, "Krzysztof", "Figiel", 2);')
cur.execute('INSERT INTO Ocena (ocenaid, studentid, przedmiotid, Ocena) VALUES (1, 1, 1, 3), (2, 1, 2, 4), (3, 1, 3, 5), (4, 1, 4, 2), (5, 1, 5, 4), (6, 2, 1, 3), (7, 2, 2, 4), (8, 2, 3, 5), (9, 2, 4, 2), (10, 2, 5, 4), (11, 3, 1, 3), (12, 3, 2, 4), (13, 3, 3, 5), (14, 3, 4, 2), (15, 3, 5, 4), (16, 4, 1, 3), (17, 4, 2, 4), (18, 4, 3, 5), (19, 4, 4, 2), (20, 4, 5, 4), (21, 5, 1, 3), (22, 5, 2, 4), (23, 5, 3, 5), (24, 5, 4, 2), (25, 5, 5, 4), (26, 6, 1, 3), (27 ,6, 2, 4), (28, 6, 3, 5), (29, 6, 4, 2), (30, 6, 5, 4)')
con.commit()
con.close()
