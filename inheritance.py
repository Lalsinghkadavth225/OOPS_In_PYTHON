class Baseplayer:
    def __init__(self,hp):
        self.hp=hp

    def walk(self):
        print("I am Walking")
class wizard(Baseplayer):
    pass
Wizard=wizard(9)
Wizard.walk()
class Archer(Baseplayer):
    def shoot(self):
        print('Shoor begins...')
class play(Baseplayer):
    def now_play(self):
        print('Playing started now ')
Archer1=Archer(8)
Player1=play(9)
Player1.now_play()
play1=Archer(2)
play1.shoot()
Archer1.walk()