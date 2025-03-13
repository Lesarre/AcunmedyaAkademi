# fonksiyonlar

def hesap_mak(a,b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    
    if b == 0:
        print("sıfır ile bölüm yapılamaz")

    
hesap_mak(10, 5)
hesap_mak(20, 3)
hesap_mak(62, 28)

# palindrom

kelime = input("kelimenizi giriniz: ")
baslangıc = len(kelime) - 1

kelime2 = ""
for index in kelime:
    kelime2 += kelime[baslangıc]
    baslangıc -= 1
print(kelime2)
if kelime == kelime2:
    print("girdiğiniz kelime palindromdur")
else:
    print("girdiğiniz kelime palindrom değildir")

# kullanıcı kaç yıl sonra 100 yaşına girecek

def yas_hesap(a):
    if a <= 0:
        return "geçerli bir yaş giriniz"
    if a >= 100:
        return "zaten yüz yaşını geçmişssiniz"
    if a < 100:
        return f"siz {100 - a} yıl sonra 100 yaşına gireceksiniz"

a = int(input())
sonuc = yas_hesap(a)
print(sonuc)





































