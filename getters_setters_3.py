import time

class Archer:
    def __init__(self, hp, dmg):
        self._hp = hp
        self._dmg = dmg
        self.crit = 1.4
        self._overall_damage = None  # Initially set to None, will be computed later.
    @property
    def dmg(self):
        return self._dmg
    @dmg.setter
    def dmg(self, value):
        self._dmg = value  # Just update _dmg, no need to reset overall damage.
    @property
    def overall_damage(self):
        # Compute the overall damage only if it hasn't been computed already.
        if self._overall_damage is None:
            print("Computing overall damage...")
            time.sleep(3)  # Simulate time-consuming computation.
            self._overall_damage = self._dmg * self.crit  # Compute and store the value.
        return self._overall_damage
# Test the Archer class
Archer1 = Archer(200, 4)
print(Archer1.overall_damage)  # This will compute and print the overall damage.
# Update the damage and check again
Archer1.dmg = 5
print(Archer1.overall_damage)  # This will recompute the overall damage because dmg was updated.
