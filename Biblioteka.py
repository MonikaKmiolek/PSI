import sys
from pprint import pprint
from pprint import pformat


#----------------------------KLASY------------------------

class Osoba:

    def __init__(self):
        self.pesel = None
        self.imie = None
        self.nazwisko = None
        self.adres_zamieszkania = None
        self.email = None




class Tytul:
    def __init__(self):
        self.autor = None
        self.tytul = None
        self.wydawnictwo = None
        self.ISBN = None


    def dodajRezerwacje(self, klient, tytul):

        if klient.rezerwacja1 is None:
            klient.rezerwacja1 = Rezerwacja()
            klient.rezerwacja1.id_kartyKlienta = klient.IdKlienta
            klient.rezerwacja1.tytul = tytul.tytul
            klient.rezerwacja1.autor = tytul.autor
            klient.rezerwacja1.dataOdKiedy = input("Podaj datę rezerwacji\n")
            print('Rezerwacja dokonana')

        elif klient.rezerwacja2 is None:
            klient.rezerwacja2 = Rezerwacja()
            klient.rezerwacja2.id_kartyKlienta = klient.IdKlienta
            klient.rezerwacja2.tytul = tytul.tytul
            klient.rezerwacja2.autor = tytul.autor
            klient.rezerwacja2.dataOdKiedy = input("Podaj datę rezerwacji\n")
            print('Rezerwacja dokonana')

        elif klient.rezerwacja3 is None:
            klient.rezerwacja3 = Rezerwacja()
            klient.rezerwacja3.id_kartyKlienta = klient.IdKlienta
            klient.rezerwacja3.tytul = tytul.tytul
            klient.rezerwacja3.autor = tytul.autor
            klient.rezerwacja3.dataOdKiedy = input("Podaj datę rezerwacji\n")
            print('Rezerwacja dokonana')

        else:
            print("Wykorzystano maksymalną ilość rezerwacji")


    def usunRezerwacje(self, rezerwacja):
        pass


class Egzemplarz(Tytul):
    def __init__(self):
        Tytul.__init__(self)
        self.nrId = None
        self.wydanie = None
        self.status = 'Dostępny'

    def wypozyczEgzemplarz(self,klient):
        if klient.wypozyczenie1 is None:
            klient.wypozyczenie1 = Wypożyczenie()
            klient.wypozyczenie1.id_kartyKlienta = klient.IdKlienta
            klient.wypozyczenie1.nrEgzemplarza = self.nrId
            klient.wypozyczenie1.dataOdKiedy = None
            klient.wypozyczenie1.dataDoKiedy = None
            self.status = 'Wypożyczony'
            print('Dokonano wypożyczenia')
        else:
            print("Wykorzystano maksymalną ilość wypożyczeń")

    def usunWypozyczenie(self,klient):
        if klient.wypozyczenie1 is not None:
            klient.wypozyczenie1 = None
            self.status = 'Dostępny'
            print("Egzemplarz został zwrócony")


class Katalog:

    def __init__(self, listatytulow, listaegzemplarzy):
        self.dostepnetytuly = listatytulow
        self.dostepneegzemplarze = listaegzemplarzy


    def przegladajTytuly(self):
        print('\nLista dostępnych tytułów:')
        print("================================")


        for x in self.dostepnetytuly:
            y = x.__dict__.items()
            for key,value in y:
                print(key,":",value)
            print('\n')


    def wyszukajTytul(self, szukanyTytul):
        jest = False

        for x in self.dostepnetytuly:
            if szukanyTytul==x.tytul:
                print("Pozycja: '", szukanyTytul, "' jest dostępna\n")
                jest = True
                break
        if jest==False:
            print("Brak podanego tytułu\n")
                
            

    def wyszukajEgzemplarz(self, szukanyEgzemplarz):
        jest = False

        for x in self.dostepneegzemplarze:
            if szukanyEgzemplarz==x.tytul:
                print("Wyszukiwany egzemplarz '", szukanyEgzemplarz,
                      "' jest dostępny.\n")
                jest = True
                break
        if jest==False:
            print("Brak egzemplarzy danego tytułu\n")

            

    def dodajTytul(self, dodawanaKsiazka):
        self.dodawanaKsiazka = Tytul
        self.dostepnetytuly.append(dodawanaKsiazka)
        print('Tytuł został dodany!')
        

    def usunTytul(self, usuwanaKsiazka):
        byl = False

        for x in self.dostepnetytuly:
            if usuwanaKsiazka==x.tytul:
                self.dostepnetytuly.remove(x)
                print("Tytuł",usuwanaKsiazka, "został usunięty z listy\n")
                byl = True
                break
        if byl==False:
            print("Podany tytuł nie istnieje na liście\n")
        

    def dodajEgzemplarz(self, dodawanyEgzemplarz):
        self.dostepneegzemplarze.append(dodawanyEgzemplarz)
        print('Egzemplarz został dodany!')
        

    def usunEgzemplarz(self, usuwanyEgzemplarz):
        bylEgzemplarz = False
        for x in self.dostepneegzemplarze:
            if usuwanyEgzemplarz==x.nrId:
                self.dostepneegzemplarze.remove(x)
                print('Egzemplarz został usunięty!')
                bylEgzemplarz = True
        if bylEgzemplarz==False:
            print('Biblioteka nie posiada danego egzemplarza')

        


class PracownikBiblioteki(Osoba):
    def __init__(self):
        Osoba.__init__(self)
        self.pozycja = None

    def szukanyTytul(self):
        print('Podaj tytuł, który chcesz wyszukać:')
        self.ksiazka = input()
        return self.ksiazka

    def szukanyEgzemplarz(self):
        print('Podaj tytuł egzemplarza, który chcesz wyszukać:')
        self.egzemplarz = input()
        return self.egzemplarz
    

    def dodajTytulPracownik(self):
        self.book = Tytul()
        print('Wprowadż tytuł, który chcesz dodać\n')
        self.book.tytul = input()
        print("Wprowadź autora książki\n")
        self.book.autor = input()
        print("Wprowadź wydawnictwo książki\n")
        self.book.wydawnictwo = input()
        print("Wprowadź numer ISBN\n")
        self.book.ISBN = input()
        return self.book


    def usunTytulPracownik(self):
        print("Wprowadź tytuł, który chcesz usunąć\n")
        self.usuwanyTytul = input()
        return self.usuwanyTytul
    

    def dodajEgzemplarzPracownik(self):
        self.item = Egzemplarz()
        print('Wprowadż tytuł egzemplarza')
        self.item.tytul = input()
        print("Wprowadź autora książki")
        self.item.autor = input()
        print("Wprowadź wydawnictwo książki")
        self.item.wydawnictwo = input()
        print("Wprowadź numer ISBN")
        self.item.ISBN = input()
        print("Wprowadź numer identyfikacyjny egzemplarza")
        self.item.nrId = input()
        print("Wprowadź wydanie egzemplarza")
        self.item.wydanie = input()
        return self.item

    def usunEgzemplarzPracownik(self):
        print('Wprowadź numer identyfikacyjny egzemplarza, który chcesz usunąć:')
        self.nrId = input()
        return self.nrId




class KlientBiblioteki(Osoba):
    def __init__(self):
        Osoba.__init__(self)
        self.IdKlienta = None
        self.DataDolaczenia = None

        self.rezerwacja1 = None
        self.rezerwacja2 = None
        self.rezerwacja3 = None

        self.wypozyczenie1 = None



class Rezerwacja(object):

    def __init__(self):
        self.id_kartyKlienta = None
        self.tytul = None
        self.autor = None
        self.dataOdKiedy = None
        self.dataDoKiedy = None


    



class Wypożyczenie(object):

    def __init__(self):
        self.id_kartyKlienta = None
        self.nrEgzemplarza = None
        self.dataOdKiedy = None
        self.dataDoKiedy = None


#----------------------ZMIENNE--------------------------
    
#Tytuły
tytul1 = Tytul()
tytul1.autor = 'Jan Galaxy'
tytul1.tytul = 'Gwiezdne wojny I'
tytul1.wydawnictwo = 'Pwn'
tytul1.ISBN = '5126'
        
tytul2 = Tytul()
tytul2.autor = 'Maryla Galaxy'
tytul2.tytul = 'Gwiezdne wojny II'
tytul2.wydawnictwo = 'Pwn'
tytul2.ISBN = '6271'

tytul3 = Tytul()
tytul3.autor = 'J.K.Rowling'
tytul3.tytul = 'Harry Potter'
tytul3.wydawnictwo = 'Media Rodzina'
tytul3.ISBN = '2178'

tytul4 = Tytul()
tytul4.autor = 'L.M.Montgomery'
tytul4.tytul = 'Ania z zielonego wzgórza'
tytul4.wydawnictwo = 'Wydawnictwo M. Arcta '
tytul4.ISBN = '8930'

tytul5 = Tytul()
tytul5.autor = "P.J.D'Adamo"
tytul5.tytul = 'Żyj zgodnie ze swoją grupą krwi'
tytul5.wydawnictwo = 'Wydawnictwo Mada '
tytul5.ISBN = '2891'


#Egzemplarze
gwiezdneWojnyI_egz1 = Egzemplarz()
gwiezdneWojnyI_egz1.autor = 'Jan Galaxy'
gwiezdneWojnyI_egz1.tytul = 'Gwiezdne wojny I'
gwiezdneWojnyI_egz1.wydawnictwo = 'Pwn'
gwiezdneWojnyI_egz1.ISBN = '5126'
gwiezdneWojnyI_egz1.nrId = '142'
gwiezdneWojnyI_egz1.wydanie = '1999'

gwiezdneWojnyI_egz2 = Egzemplarz()
gwiezdneWojnyI_egz2.autor = 'Jan Galaxy'
gwiezdneWojnyI_egz2.tytul = 'Gwiezdne wojny I'
gwiezdneWojnyI_egz2.wydawnictwo = 'Pwn'
gwiezdneWojnyI_egz2.ISBN = '5126'
gwiezdneWojnyI_egz2.nrId = '615'
gwiezdneWojnyI_egz2.wydanie = '2000'

gwiezdneWojnyI_egz3 = Egzemplarz()
gwiezdneWojnyI_egz3.autor = 'Jan Galaxy'
gwiezdneWojnyI_egz3.tytul = 'Gwiezdne wojny I'
gwiezdneWojnyI_egz3.wydawnictwo = 'Pwn'
gwiezdneWojnyI_egz3.ISBN = '5126'
gwiezdneWojnyI_egz3.nrId = '627'
gwiezdneWojnyI_egz3.wydanie = '2001'

#Katalog
katalog = Katalog([tytul1, tytul2, tytul3, tytul4, tytul5],
                  [gwiezdneWojnyI_egz1, gwiezdneWojnyI_egz2,
                   gwiezdneWojnyI_egz3])


#Pracownicy
pracownik = PracownikBiblioteki()
pracownik.pesel = 83457857
pracownik.imie = 'Anna'
pracownik.nazwisko = 'Kowal'
pracownik.adres_zamieszkania = 'Diamentowa 47 56-320 Wrocław'
pracownik.email = 'ankaskakanka@gmail.com'
pracownik.pozycja = 'dyrektor'

#Klienci
klient1 = KlientBiblioteki()
klient1.pesel = 834523
klient1.imie = 'Piotr'
klient1.nazwisko = 'Głowacki'
klient1.adres_zamieszkania = 'Rubinowa 36 56-320 Wrocław'
klient1.email = 'piotrek.buziaczek@gmail.com'
klient1.IdKlienta= 100
klient1.DataDolaczenia = '14.06.2014'

klient2 = KlientBiblioteki()
klient2.pesel = 130944
klient2.imie = 'Małgorzata'
klient2.nazwisko = 'Pietraś'
klient2.adres_zamieszkania = 'Grzybowska 13/4 Wrocław'
klient2.email = 'malgosia.piet@gmail.com'
klient2.IdKlienta= 132
klient2.DataDolaczenia = '13.07.2014'

klienci = [klient1,klient2]


#-------------------------------FUNKCJE------------------------------------

def main():

    done = False
    while done == False:
        print("""\n====== Menu bibliotekarza =====
        1. Wyświetl dostępne pozycje
        2. Wyszukaj tytuł
        3. Wyszukaj egzemplarz
        4. Dodaj Tytuł
        5. Usuń tytuł
        6. Dodaj Egzemplarz
        7. Usuń Egzemplarz
        8. Wróć do menu głównego\n""")
        choice = int(input('Wybierz cyfrę opcji:'))
        if choice == 1:
            katalog.przegladajTytuly()
        elif choice == 2:
            katalog.wyszukajTytul(pracownik.szukanyTytul())
        elif choice == 3:
            katalog.wyszukajEgzemplarz(pracownik.szukanyEgzemplarz())
        elif choice == 4:
            katalog.dodajTytul(pracownik.dodajTytulPracownik())
        elif choice == 5:
            katalog.usunTytul(pracownik.usunTytulPracownik())
        elif choice == 6:
            katalog.dodajEgzemplarz(pracownik.dodajEgzemplarzPracownik())
        elif choice == 7:
            katalog.usunEgzemplarz(pracownik.usunEgzemplarzPracownik())
        elif choice == 8:
            done = True




def main1():
    
    doneK = False
    while doneK == False:
        print("""\n====== Menu klienta =====
        1. Wyświetl dostępne pozycje
        2. Wyszukaj tytuł
        3. Wyszukaj egzemplarz
        4. Zarezerwuj
        5. Wypożycz
        6. Zwróć książkę
        7. Wróć do menu głównego\n""")
        choiceK = int(input('Wybierz cyfrę:'))
        if choiceK == 1:
            katalog.przegladajTytuly()
            
        elif choiceK == 2:
            print('Podaj tytuł, który chcesz wyszukać:')
            szukanyTytulKlient = input()
            katalog.wyszukajTytul(szukanyTytulKlient)
            
        elif choiceK == 3:
            print('Podaj tytuł egzemplarza, który chcesz wyszukać:')
            egzemplarzKlient = input()
            katalog.wyszukajEgzemplarz(egzemplarzKlient)
            
        elif choiceK == 4:
            print('Podaj swój numer ID')
            nrKlienta = input()

            jestKlient = False
            for x in klienci:
                if int(nrKlienta)==x.IdKlienta:
                    jestKlient= True
                    print('Podaj tytuł, który chcesz zarezerwować')
                    rezerwowanyTytul = input()

                    jestTytul = False
                    for y in katalog.dostepnetytuly:
                        if rezerwowanyTytul==y.tytul:
                            y.dodajRezerwacje(x,y)
                            jestTytul = True
                            break
                    if jestTytul==False:
                        print("Brak danego tytułu\n")


            if jestKlient==False:
                print("Niezarejestrowany klient\n")
                
        elif choiceK == 5:
            print('Podaj swój numer ID')
            nrKlienta = input()

            jestKlient = False
            for x in klienci:
                if int(nrKlienta)==x.IdKlienta:
                    jestKlient= True
                    print('Podaj numer egzemplarza, który chcesz wypożyczyć')
                    wypozyczanyEgzemplarz = input()

                    jestEgzemplarz = False
                    for y in katalog.dostepneegzemplarze:
                        if wypozyczanyEgzemplarz==y.nrId:
                            jestEgzemplarz = True
                            if y.status=='Dostępny':
                                y.wypozyczEgzemplarz(x)
                            else:
                                print("Przepraszamy, ale egzemplarz został już wypożyczony")
                            
                    if jestEgzemplarz==False:
                        print("Biblioteka nie posiada danego egzemplarza\n")
            if jestKlient==False:
                print("Niezarejestrowany klient\n")
        elif choiceK ==6:
            print('Podaj swój numer ID')
            nrKlienta = input()

            jestKlient = False
            for x in klienci:
                if int(nrKlienta)==x.IdKlienta:
                    jestKlient= True
                    print('Podaj numer egzemplarza, który chcesz oddać')
                    zwracanyEgzemplarz = input()

                    jestEgzemplarz = False
                    for y in katalog.dostepneegzemplarze:
                        if zwracanyEgzemplarz==y.nrId:
                            jestEgzemplarz = True
                            if y.status=='Wypożyczony':
                                y.usunWypozyczenie(x)
                            else:
                                print("Przepraszamy, ale egzemplarz został już zwrócony")
                    if jestEgzemplarz==False:
                        print("Biblioteka nie posiada danego egzemplarza\n")
            if jestKlient==False:
                print("Niezarejestrowany klient\n")
        elif choiceK ==7:
            doneK = True



done0 = False
while done0 == False:
    print("""\nWitaj w systemie biblioteki, wybierz tryb, z którego chcesz skorzystać:
         1. Bibliotekarz
         2. Klient
         3. Zamknij\n""")
    choice0 = int(input('Wybierz cyfrę:'))
    if choice0 == 1:
        main()
    elif choice0 == 2:
        main1()
    elif choice0 == 3:
        done0 = True
        print("------ Do zobaczenia ------")



sys.exit()
