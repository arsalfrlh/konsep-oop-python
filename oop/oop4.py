class Hero:
    def __init__(self, heroName, heroHealt, heroAtk, heroDef): #konstruktor| this dan prameter heroName, heroHealt, heroAtk
        self.name = heroName #membuat variabel this name dan isinya parameter konstruktor
        self.healt = heroHealt
        self.atk = heroAtk
        self.defense = heroDef

    def serang(self, lawan): #this dan parameter class
        print(self.name + " meneyerang " + lawan.name) #variabel this name dan isinya parameter heroName| menyerang| parameter class dan isi variabel name
        lawan.diserang(kwanzaa, self.atk) #setelah mengeksekusi di atas kita memanggil function diserang

    def diserang(self, lawan, damage):
        print(self.name + " diserang " + lawan.name)
        totalDamage = damage/self.defense
        print("Damage diterima: " + str(totalDamage))
        self.healt -= totalDamage
        print("Darah " + self.name + " tersisa " + str(self.healt))

    # def diserang(self, Namalawan):
    #     print(self.name + " diserang " + Namalawan)

kwanzaa = Hero("Kwanzaa", 100, 10, 5)
arsal = Hero("Arsal", 85, 15, 10)

kwanzaa.serang(arsal) #class Hero kwanzaa memanngil void function serang| parameter class Hero arsal
print("\n")
arsal.serang(kwanzaa) #class Hero kwanzaa memanngil void function serang| parameter class Hero kwanzaa
print("\n")
kwanzaa.serang(arsal)
print("\n")
arsal.serang(kwanzaa) 
print("\n")
kwanzaa.serang(arsal)
print("\n")
arsal.serang(kwanzaa) 
# arsal.diserang(kwanzaa.name) #bisa juga seperti ini
    
#hasilnya
# Kwanzaa meneyerang Arsal
# Arsal diserang Kwanzaa
# Damage diterima: 1.0
# Darah Arsal tersisa 84.0


# Arsal meneyerang Kwanzaa
# Kwanzaa diserang Kwanzaa
# Damage diterima: 3.0
# Darah Kwanzaa tersisa 97.0


# Kwanzaa meneyerang Arsal
# Arsal diserang Kwanzaa
# Damage diterima: 1.0
# Darah Arsal tersisa 83.0


# Arsal meneyerang Kwanzaa
# Kwanzaa diserang Kwanzaa
# Damage diterima: 3.0
# Darah Kwanzaa tersisa 94.0


# Kwanzaa meneyerang Arsal
# Arsal diserang Kwanzaa
# Damage diterima: 1.0
# Darah Arsal tersisa 82.0


# Arsal meneyerang Kwanzaa
# Kwanzaa diserang Kwanzaa
# Damage diterima: 3.0
# Darah Kwanzaa tersisa 91.0
    