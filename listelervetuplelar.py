# listeler ve tuple'lar

import numpy as np

sayi1 = int(input("lütfen ilk sayınızı giriniz: "))
sayi2 = int(input("lütfen ikinci sayınızı giriniz: "))
sayi3 = int(input("lütfen üçüncü sayınızı giriniz: "))
sayi4 = int(input("lütfen dördüncü sayınızı giriniz: "))
sayi5 = int(input("lütfen beşinci sayınızı giriniz: "))

sayilar = []

sayilar.append(sayi1)
sayilar.append(sayi2)
sayilar.append(sayi3)
sayilar.append(sayi4)
sayilar.append(sayi5)

print(np.sum(sayilar))
print(np.mean(sayilar))
print(np.max(sayilar))
print(np.min(sayilar))


# kelimeleri listeye ekleme ve ters yazdırma

kelime1 = input("kelimenizi giriniz: ")
kelime2 = input("kelimenizi giriniz: ")
kelime3 = input("kelimenizi giriniz: ")
kelime4 = input("kelimenizi giriniz: ")
kelime5 = input("kelimenizi giriniz: ")

kelimeler = []

kelimeler.extend([kelime1,kelime2,kelime3,kelime4,kelime5])
kelimeler.reverse()
print(kelimeler)

#liste içindeki tekrar eden elemanları kaldırma

arabalar = np.array(["bmw","audi","fiat","bmw","porsche","fiat","bugatti","audi","seat","jaguar"])
temiz_dizi = np.unique(arabalar)
print(temiz_dizi)
























