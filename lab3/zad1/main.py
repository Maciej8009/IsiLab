import sqlite3


con = sqlite3.connect("Uczelnie.db")
cur = con.cursor()
cur.execute('CREATE TABLE Uczelnia (UczelniaID INT NOT NULL, Uczelnia_Nazwa VARCHAR NOT NULL, Adres VARCHAR NOT NULL, PRIMARY KEY (UczelniaID))')
cur.execute('CREATE TABLE Wydział (WydziałID INT NOT NULL, Wydział_nazwa VARCHAR NOT NULL, UczelniaID INT NOT NULL, PRIMARY KEY (WydziałID), FOREIGN KEY (UczelniaID) REFERENCES Uczelnia(UczelniaID))')
cur.execute('CREATE TABLE Grupa_studencka (GrupaID INT NOT NULL, GrupaNazwa VARCHAR NOT NULL, WydziałID VARCHAR NOT NULL, PRIMARY KEY (GrupaID), FOREIGN KEY (WydziałID) REFERENCES Wydział(WydziałID))')
cur.execute('CREATE TABLE Wykładowca (WykładowcaID INT NOT NULL, Imie VARCHAR NOT NULL, Nazwisko VARCHAR NOT NULL, WydziałID INT NOT NULL, PRIMARY KEY (WykładowcaID), FOREIGN KEY (WydziałID) REFERENCES Wydział(WydziałID))')
cur.execute('CREATE TABLE Przedmiot (PrzedmiotID INT NOT NULL,Przedmiot_Nazwa VARCHAR NOT NULL,WykładowcaID INT NOT NULL,PRIMARY KEY (PrzedmiotID),FOREIGN KEY (WykładowcaID) REFERENCES Wykładowca(WykładowcaID))')
cur.execute('CREATE TABLE Student (StudentID INT NOT NULL, Imie VARCHAR NOT NULL, Nazwisko VARCHAR NOT NULL, GrupaID INT, PRIMARY KEY (StudentID), FOREIGN KEY (GrupaID) REFERENCES Grupa_studencka(GrupaID))')
cur.execute('CREATE TABLE Ocena (OcenaID INT NOT NULL, Ocena INT NOT NULL, StudentID INT NOT NULL, PrzedmiotID INT NOT NULL, PRIMARY KEY (OcenaID), FOREIGN KEY (StudentID) REFERENCES Student(StudentID),FOREIGN KEY (PrzedmiotID) REFERENCES Przedmiot(PrzedmiotID))')
con.close()