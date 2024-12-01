class Archer:
    __slots__ = ("hp","mana")

    def __init__(self,hp,mana):
        self.hp=hp
        self.mana=mana

class Archer2:
    # __slots__ = ("hp,"mana")

    def __init__(self, hp, mana):
        self.hp = hp
        self.mana = mana

Archer1 = Archer(20, 3)
Archer2=Archer2(4,3)

from pympler import asizeof
print(asizeof.asizeof(Archer1))
print(asizeof.asizeof(Archer1))