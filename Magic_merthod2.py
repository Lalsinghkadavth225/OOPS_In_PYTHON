import uuid

class Archer:
    def __init__(self,hp,mana,arrows):
        self.hp=hp
        self.arrows=arrows
        self.mana=mana
    def __hash__(self):
        return hash(self.hp,self.arrows,self.mana)

Archer1=Archer(4,8,9)
Archer1=Archer(4,8,9)
