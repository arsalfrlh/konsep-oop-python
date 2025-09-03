class Hero: #class
    jumlah = 0 #class variabel| (variabel class ini akan nempel di classnya)
    def __init__(self, heroName, heroHealt, heroAtk): #konstruktor| this dan prameter heroName, heroHealt, heroAtk
        self.name = heroName #membuat variabel this name dan isinya parameter dari konstruktor
        self.healt = heroHealt #(variabel objek ini akan nempel di objek yg di panggil)
        self.atk = heroAtk
        Hero.jumlah += 1 #jumlahnya akan di tambahkan 1 setiap konstruktor ini di panggil| class dan konstruktor ini di panggil 3x pd variabel (hero,hero2,hero3)
        print("Membuat Hero dengan Nama " + heroName)

hero = Hero("Kwanzaa", 100, 10) #saat saya memanggil variabel ini akan menjalankan class dan konstruktor yg di atas
print(Hero.jumlah)
hero2 = Hero("Arsal", 85, 15)
print(Hero.jumlah)
hero3 = Hero("Fahrulloh", 120, 5)
print(Hero.jumlah)

#hasilnya
# Membuat Hero dengan Nama Kwanzaa
# 1
# Membuat Hero dengan Nama Arsal
# 2
# Membuat Hero dengan Nama Fahrulloh
# 3