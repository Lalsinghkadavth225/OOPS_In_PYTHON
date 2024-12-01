import uuid
class Archer:
    def __init__(self,mana,hp,arrows):
        self.arrows=arrows
        self.mana=mana
        self.hp=hp
        self.uuid=uuid.uuid4()
    def __eq__(self,other):
        if not isinstance(other,Archer):
            return NotImplemented

        return self.mana==other.mana and self.hp==other.hp and self.arrows==other.arrows
    def __lt__(self, other):
        if not isinstance(other, Archer):
            return NotImplemented

        return self.mana < other.mana and self.hp < other.hp and self.arrows < other.arrows

    def __gt__(self, other):
        if not isinstance(other, Archer):
            return NotImplemented

        return self.mana > other.mana and self.hp > other.hp and self.arrows > other.arrows
    def __hash__(self):
        return(hash((self.mana,self.hp,self.arrows)))

Archer1=Archer(2,4,5)
Archer2=Archer(2,4,5)
print(hash(Archer1))
print(Archer1==Archer2)
print(Archer1<Archer2)
print(Archer1>Archer2)
self.hana=200
print(hash(Archer1))
new_dict={Archer1:"Test"}
