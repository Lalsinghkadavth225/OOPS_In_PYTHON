class Baseplayer:
    def __init__(self, hp):
        self.hp = hp  # Initialize health points

class Archer(Baseplayer):
    def __init__(self, hp, arrows):  # Corrected the typo in __init__
        Baseplayer.__init__(self, hp=hp)
        # super().__init__(hp)  # Call the parent class constructor
        self.arrows = arrows  # Initialize arrows

    def shoot(self):
        if self.arrows > 0:
            self.arrows -= 1  # Reduce the number of arrows by 1
            print(f"Shoot begins! {self.arrows} arrows left!")
        else:
            print("Out of arrows!")

# Create an instance of Archer
Archer1 = Archer(2, 3)

# Call the shoot method twice
Archer1.shoot()
Archer1.shoot()
Archer1.shoot()
Archer1.shoot()  # Attempt to shoot with no arrows left
