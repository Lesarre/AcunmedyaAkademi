# tek mi cift mi

sayi = int(input("sayınızı giriniz: "))

if sayi % 2 == 0:
    print("sayı çifttir")
else:
    print("sayı tektir")


# not hesaplama

kul_not = int(input("lütfen notunuzu giriniz: "))

if kul_not >= 90 and kul_not <= 100:
    print("harf notunuz A")
if kul_not >= 80 and kul_not <= 89:
    print("harf notunuz B")
if kul_not >=70 and kul_not <= 79:
    print("harf notunuz C")
if kul_not >= 60 and kul_not <= 69:
    print("harf notunuz D")
if kul_not <= 59:
    print("harf notunuz F")

# yas grubu bulma

yas = int(input("lütfen yaşınızı giriniz: "))

if yas >= 0 and yas <= 12:
    print("kullanıcı çocuk grubundadır")
if yas >= 13 and yas <= 19:
    print("kullanıcı genç yaş grubundadır")
if yas >= 20 and yas <= 59:
    print("kullanıcı yetişkin yaş grubundadır")    
if yas >= 60:
    print("kullanıcı yaşlı grubundadır")































