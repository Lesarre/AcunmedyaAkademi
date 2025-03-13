#1'den 100'e

for i in range(1,100):
    print(i)

#1'den 100'e çift sayı

for i in range(1,100):
    if i % 2 == 0:
        print(i)

#faktöriyel

sayi = int(input("lütfen faktöriyelinin hesaplanmasını istediğiniz sayıyı giriniz: "))
factorial = 1
i = 1
if sayi >= 0:
    while i <= sayi:
        factorial *= i
        i += 1
    print("girdiğiniz sayının faktöriyeli: " , factorial)
else:
    print("lütfen pozitif bir sayı giriniz!!!")


# asal sayı bulma

for i in range (2,100):
    if i == 2 or i == 5 or i == 3 or i == 7:
        print(i)
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        print(i)







































