class Hero: #class
    def __init__(self, heroName, heroHealt, heroAtk): #konstruktor| this dan prameter heroName, heroHealt, heroAtk
        self.name = heroName #membuat variabel this name dan isinya parameter konstruktor
        self.healt = heroHealt
        self.atk = heroAtk

hero = Hero("Kwanzaa", 100, 10) #variabel hero menyimpan class dan isi parameter konstruktornya| saat saya memanggil ini akan menjalankan class dan konstruktor yg di atas
hero2 = Hero("Arsal", 85, 15)
hero3 = Hero("Fahrulloh", 120, 5)

print("Karakter Pertama")
print(hero.name) #memanggil variabel name yg ada di class di atas
print(hero.healt)
print(hero.atk)

print("Karakter ke dua") #contoh hasilnya
print(hero2.name) #Arsal
print(hero2.healt) #85
print(hero2.atk) #15

print("Karakter ke tiga")
print(hero3.name)
print(hero3.healt)
print(hero3.atk)

print(hero.__dict__) #menampilkan semua data tanpa perlu menggunkan variabel di dalam class| contoh {'name': 'Kwanzaa', 'healt': 100, 'atk': 10}
print(hero2.__dict__)
print(hero3.__dict__)