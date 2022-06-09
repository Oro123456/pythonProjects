## Tworzenie tablicy
Do tworzenia tablicy można wykorzystać szereg funkcji Numpy, m.in:
* np.array - podanie wartości
* np.arange - zakres liczbowy z odstępem między liczbami
* np.linspace - zakres z liczbą liczb na który go dzielimy
* np.random.random - uzupełnienie wartościami losowymi

print(np.array([x for x in range(11) if x%2==0]))
print(np.arange(0,11,2))
print(np.linspace(0,10,6))

## Indeksowanie tablic
Indeksowanie tablic odbywa się w analogiczny sposób jak w przypadku list. W tym przypadku pierwszy element również ma indeks 0. 
W przypadku tablicy jednowymiarowej pierwszy element otrzymany przez nazwa_tablicy[0]. W przypadku większej liczby wymiarów indeksujemy
przez listę indeksów, np. nazwa_tablicy[0,1,2]. Do sprawdzenia liczby wymiarów używamy nazwa_tablicy.ndim, a do sprawdzenia rozmiaru
nazwa_tablicy.shape.

tablica.ndim
tablica.shape


## Obliczenia statystyczne
Biblioteka Numpy zawiera możliwość szeregu obliczeń statystycznych takich jak:
* średnia
* mediana
* odchylenie standardowe
* macierz korelacji

