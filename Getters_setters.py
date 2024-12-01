class Archer:
    def __init__(self, hp):
        self._hp = hp

    def get_hp(self):
        print("getter called ")
        return self._hp

    def set_hp(self, value):
        if value > 200:
            raise ValueError("The value cannot be more than 200")
        self._hp = value  # Set the value to the internal variable

    hp = property(fget=get_hp, fset=set_hp)  # Define the property here

Archer1 = Archer(200)
print(Archer1.hp)  # Access the property
Archer1.hp = 150  # Set the property
print(Archer1.hp)  # Access the updated property
