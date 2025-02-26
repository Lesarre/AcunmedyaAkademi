# asal sayı

def asal_mi(sayi):
    if sayi < 2:
       return False
    for i in range(2,sayi):
        if sayi % i == 0:
           return False
    return True

sayi = int(input("Lütfen bir sayı giriniz: "))

if asal_mi(sayi):
    print("Sayı asaldır")
else:
    print("sayı asal değildir")


#hesap makinesi

def hesap_makinesi():
    a = float(input("Birinci sayıyı giriniz: "))
    b = float(input("İkinci sayıyı giriniz: "))

    islemler = ["+", "-", "*", "/"]
    islem = input("Lütfen yapmak istediğiniz işlemi seçiniz: " + str(islemler) + " ")

    if islem not in islemler:
        print("Geçersiz işlem!")
    
    if islem == "+":
        print("Sonuç:", a + b)
    elif islem == "-":
        print("Sonuç:", a - b)
    elif islem == "*":
        print("Sonuç:", a * b)
    elif islem == "/":
        if b == 0:
            print("ikinci sayı sıfır olamaz")
        print("Sonuç:", a / b)


hesap_makinesi()








































