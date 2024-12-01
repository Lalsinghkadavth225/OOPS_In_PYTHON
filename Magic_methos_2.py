class Archer:
    def __init__(self,mana,hp,arrows):
        self.arrows=arrows
        self.hp=hp
        self.mana=mana
    def __hash__(self):
        return hash((self.mana,self.hp,self.arrows))
Archer1=Archer(20,30,40)
Archer2=Archer(20,30,40)

new_dict={Archer1: "Test"}
print(Archer1)
