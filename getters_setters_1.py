class Archer:
    def __init__(self,hp,dmg):
        self._hp=hp
        self._dmg=dmg
        self.crit=1.4
        self._overall_damage=self._dmg * self.crit

    @property
    def dmg(self):
        return self._dmg
Archer1=Archer(200,20)
print(Archer1._overall_damage)
