class Hero: #class
    jumlah = 0 #class variabel
    def __init__(self, heroName, heroHealt, heroAtk): #konstruktor| this dan prameter heroName, heroHealt, heroAtk
        self.name = heroName
        self.healt = heroHealt
        self.atk = heroAtk
        Hero.jumlah += 1
    
    #void function| methode tanpa return dan argument| function dlm class
    def siapa(self): #this
        print("Namaku Adalah " + self.name)

    #void function| method dengan argument
    def healtUp(self, up): #this dan parameter
        self.healt += up

    #void function| methode dengan return
    def getHealt(self):
        return self.healt


hero = Hero("Kwanzaa", 100, 10) #saat saya memanggil variabel ini akan menjalankan class dan konstruktor yg di atas
hero2 = Hero("Arsal", 85, 15)

hero.siapa()

hero.healtUp(10) #variabel berisi class ini memanggil method function (healtUp dan isi parameternya) dlm class
print(hero.healt)

print(hero.getHealt())

#hasilnya
# Namaku Adalah Kwanzaa
# 110
# 110