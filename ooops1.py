class Archer:
    def __init__(self, hp, hana, arrows):
        self.arrows = arrows
        self.hana = hana
        self.hp = hp
    def shoot(self):
        if self.arrows > 0:
            self.arrows -= 1
            print(f'Archer shot! {self.arrows} arrows left.')
        else:
            print("Sorry, no arrows left.")
    @classmethod
    def from_string(cls, data_string):
        arrows, hana, hp = map(int, data_string.split('-'))
        return cls(hp, hana, arrows)  # Note the order is important to match with the constructor
    @staticmethod
    def static():
        print("this is static method ")
# Creating an Archer instance using the from_string class method
Archer1 = Archer(6, 5, 4)
# Creating another Archer instance using the from_string method
Archer2 = Archer.from_string('6-5-4')
# Call the shoot method for Archer2
Archer2.shoot()
Archer.static()
Archer2.static()


