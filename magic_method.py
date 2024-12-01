class Archer:
    def __init__(self,hp,mana,arrows):
        self.arrows=arrows
        self.mana=mana
        self.hp=hp
    def __add__(self,other):
        if not isinstance(other,Archer):
            return NotImplemented
        new_hp=self.hp+other.hp
        new_mana=self.mana+other.mana
        new_arrows=self.arrows+other.arrows
        return new_hp,new_arrows,new_mana

archer1=Archer(4,3,6)
# archer2=Archer(4,3,6)
archer2=7
archer3=archer1+archer2
print(archer3)
