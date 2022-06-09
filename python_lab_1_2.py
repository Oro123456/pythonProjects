### Tworzenie tablicy
Do tworzenia tablicy można wykorzystać szereg funkcji Numpy, m.in:
* np.array - podanie wartości
* np.arange - zakres liczbowy z odstępem między liczbami
* np.linspace - zakres z liczbą liczb na który go dzielimy
* np.random.random - uzupełnienie wartościami losowymi



## Obliczenia w Pythonie
Działania matematyczne w Python
* '+' dodawanie
* '-' odejmowanie
* '*' mnożenie
* '/' dzielenie
* '**' potęgowanie
* '%' modulo (reszta z dzielenia)

type(varible)       # informuje jaki jest typ zmiennej 

2**4                # ptegowanie - 2 do potegi 4 
10%2                # modulo - reszta z dzielenia przez dwa 

10 / 2              # pamietaj! wynik z dzielenia jest zawsze typu 'float' =≠

## Typy danych
* Liczba całkowita (Integer)
* Liczba zmiennoprzecinkowa (Float)
* Tekst (String)
* Wartość logiczna (Boolean)
* Lista (List)
* Krotka (Tuple)
* Słownik (Dictionary)

## Deklaracja zmiennych 

Nazwy zmiennych:
* na pierwszym miejscu niecyfra
* brak spacji
* brak znaków specjalnych oprócz _
* rozróżnianie wielkości liter


## zwieksz zmienna o 1 

b+=1

## Konwersja zmiennych:
* float(nazwa_zmiennej) - konwersja na zmienną liczbową zmiennoprzecinkową
* int(nazwa_zmiennej) - konwersja na liczbę całkowitą
* str(nazwa_zmiennej) - konwersja na typ tekstowy


ex. float(b)


## Wprowadzanie zmiennych 

Do wprowadzania danych przez użytkownika służy funkcja input(), który można przypisać do zmiennej oraz wprowadzić jako argument informacje dla użytkownika.

input ()

## Drukowanie zmiennych

Drukowanie zmiennych wykonujemy przez print()

print('To jest jakis teskt do wydrukowania')

## Listy w Pythonie

Tworzenie listy odbywa się za pomocą []. Lista jest typem mutowalnym, co oznacza możliwość zmiany konkretnego elementu listy. Listy są indeksowane od zera. Elementy listy mogą być różnego typu. Elementem listy może być również inna lista.

lista=['a',1,True]

lista[0]

lista[1:2]              # wydrukuj elementy 1
lista[1:3]              # wydrukuj element 1 oraz 2 
lista[1:]               # wydrukuj od 1 do końca listy
lista[:2]               # wydrukuj od poczatku do 3 elementu listy (bez 3 elementu)
lista[:-1]              # wydrukuj wszystkie do elementu liczac od konca (wszystkie bez ostatniego elementu -1, bez dwoch ostatnich elementow -2 etc)
listalist=[[1,2,3],[4,5,6],[7,8,9]]
listalist[0][0]         # wyswietl element pierwszy na liscie list 

## Krotka (Tuple) w Pythonie

Innym złożonym typem danych jest krotka (tuple) tworzona za pomocą (). Typ ten jest zbliżony do listy z tym, że jest niemutowalny oraz zajmuje mniej pamięci.

tupla=('a',5,6,7,True)  # uywamy nawiasów okragłych 
tupla[1]                # ale do odwolania sie do elementow mozemy normalnie uzywac nawiasow kwadratowych. 

# wazne -> elementy na krotkach sa "niemutowalne" to znaczy ze nie mozna ich zmieniac 
# KROTKA zajmuje mniej pamieci niz LISTA

len(lista)              # dlugosc listy mozemy sprawdzic za pomoca funkcji 'len' 

# listy mozemy konwertowac na tuple i odwrotnie 
tuple(lista)
list(tupla) 

## Metody listy

Metody listy:
* append(rozszerzenie listy o element)
* extend(rozszerzenie listy o listę elementów)
* remove(usunięcie pierwszego podanego elementu z listy)
* insert(wstawienie przed określonym indeksem elementu)
* reverse(odwrócenie elementów listy)
* sort(sortowanie elementów listy)

lista.append()
lista.extend()
lista.remove()
lista.insert()
lista.reverse() 
lista.sort()

## Słownik 

Słownik przechowuje dane w parach klucz:wartość. Tworzony jest za pomocą {}. Klucz musi być typu niemutowalnego oraz unikalny w obrębie kluczy słownika. Do elementów słownika odnosi się za pomocą slownik[klucz]. W ten sposób można nadpisać również wartość słowniku oraz dodać nową parę klucz:wartość. Aby sprawdzić występowanie określonego klucza w słowniku należy użyć klucz in slownik.

slownik={'a':1,'b':2,'d':4,('a','b'):(1,2)}

## Petle i instrukcje warunkowe 

Operatory porównań w Pythonie:
* '<' mniejsze niż
* '>' większe niż
* '<=' mniejsze lub równe
* '>=' większe lub równe
* '==' równe
* '!=' nierówne
* 'and' i
* 'or' lub

## Instrukcje warunkowe
if (warunek):
    działanie
elif (warunek):
    działanie
else:
    działanie
    
elif oraz else są opcjonalne

## Pętla for
for iterator in kolekcja:
    działanie

Iterować możemy np. po liczbach używając range tworzącego zbiór liczb, elementach listy, kluczach słownikach, kolejnych znakach napisu.

for i in range(0,50,10):
    print(i)

### Pętla while
Pętla while wykonuje się do momentu spełnienia określonego warunku:

while (warunek):
    działanie

    n=0
while n<10:
    print(n)
    n+=1


### Tworzenie funkcji zdefiniowanych przez użytkownika
def nazwa_funkcji(argumenty):
    obliczenia
    return wynik_obliczeń

W ramach własnej funkcji możliwe jest utworzenie argumentów z wartościami domyślnymi przez argument=wartość. W przypadku gdy argument nie ma wartości domyślnych konieczne będzie wpisanie wartości dla danego argumentu. Wynik działania własnej funkcji można przypisać do zmiennej za pomocą nazwa_zmiennej=funkcja(argumenty). Własna funkcja może być również użyta w wyrażeniu listotwórczym. Dokumentację własnej funkcji można zapisać po jej zdefiniowaniu. Dostanie się do dokumentacji jest możliwe przez nazwa_funkcji.__doc__.

def naszafunkcja(x):
    y=x**2
    return y