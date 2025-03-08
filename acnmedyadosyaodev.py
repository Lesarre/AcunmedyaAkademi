metin = input("metninizi giriniz:")
with open ("metin.txt","a") as dosya:
    dosya.write(metin + "\n")

with open ("metin.txt","r") as dosya:
    icerik = dosya.read()
    print(icerik)

satir1 = input("satırınızı giriniz:")
satir2 = input("satırınızı giriniz:")
satir3 = input("satırınızı giriniz:")
satir4 = input("satırınızı giriniz:")
satir5 = input("satırınızı giriniz:")

with open ("metin2.txt","a") as dk:
    dk.write(satir1 +  satir2 +  satir3 +  satir4 +  satir5)

with open ("metin2.txt","r") as dkk:
    satirlar = dkk.readlines()
    print(satirlar)






























































