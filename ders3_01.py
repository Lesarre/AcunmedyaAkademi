class Human:
    name = "Lesar"
    
    def __init__(self,name):
        self.name = name
        print("bir insan örneği üretildi")
    def __str__(self):
        return f"STR fonksiyonundan dönen değer: {self.name}"
    
    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} : is walking")
    

human1 = Human()
human1.name = "Emre"
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human()
human2.name = "Latif"
human2.talk("Selam")
human2.walk()
print(human2)






























































































































