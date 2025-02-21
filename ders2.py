faiz = 1.59
vade = 36
vade2 = "35"
krediAdi = "ihtiyaç kredisi"

#type fonksiyonu

print(vade + 12)
print(int(vade2) + 12)

faiz = (str(faiz))
print(type(faiz))

vade = input("lütfen istediğiniz vade sayısını girin:")    #int(input())
print(vade) #kullanıcıdan alınan veri str
print(int(vade) + 12)
vade = vade + 12

#string interpolation
print("seçtiğiniz vade sonucu ortaya çıkan vade: ", str(vade))
print("seçtiğiniz vade sonucu ortaya çıkan vade:  {vadeSayisi}".format(vadeSayisi=vade))

isim = "Lesar"
metin = "Merhaba {name}".format(name = isim)
print(metin)

# f-string
metin = f"Hos geldiniz {1+1}"
print(metin)

#list

krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
print(krediler)
print(krediler[0])
print(krediler[2])
print(len(krediler))

dizi = ["ihtiyaç k",3,False,10.24]
print(dizi)

krediler.append("özel kredi")
print(krediler)
krediler.append("x kredisi")
print(krediler)
krediler.pop() #default olarak sen eklenen elemanı siler
print(krediler)

krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y Kredisi","Z Kredisi"])
print(krediler)

#for 

for i in range(10):
    print(i)

for i in range(5,10):
    print(i)

for i in range(0,51,10):
    print(i)

for kredi in krediler:
    print(kredi)

for i in range(len(krediler)):
    print(krediler[i])


i = 0
while i < 10:
    print("x")
    i += 1

while True:
    print("x")
    break

print("************")

i=0
while i < len(krediler):
    if krediler[i] == "Konut Kredisi":
        break
    print(krediler[i])
    i += 1

#fonksiyonlar

fiyat = 100
indirim = 20

def calculate ():
    print(100-20)    
        
calculate()  

def calculateWithParams(fiyat,indirim):
    print(fiyat - indirim)      

calculateWithParams(50,10)
calculateWithParams(100, 30)

def sayHello(name):
    print(f"Merhaba {name}")

sayHello("Lesar")
sayHello("Tuana")

def calculateAndReturn(price,discount):
    return price - discount

yeniFiyat = calculateAndReturn(200, 50)
print(yeniFiyat)








































