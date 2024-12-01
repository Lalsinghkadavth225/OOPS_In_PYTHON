class Archer:
    def __init__(self, mana, hp, arrows):
        self.mana = mana
        self.arrows = arrows
        self.hp = hp

    def __repr__(self):
        return f"Archer(mana={self.mana}, hp={self.hp}, arrows={self.arrows})"

# Define the `compony` class
class Company:
    def __init__(self, size):
        self.size = size
        self.archers = []  # List to hold Archer instances
        self.index = 0

    def add_archer(self, archer):
        # Validate the type of the input
        if not isinstance(archer, Archer):
            raise TypeError("Only Archers are allowed.")
        # Ensure the company is not full
        if len(self.archers) >= self.size:
            raise ValueError("Company is FULL.")
        self.archers.append(archer)

    def __add__(self, other):
        # Allow addition of Archer objects to the company
        if not isinstance(other, Archer):
            raise ValueError("Only Archer objects can be added to the company.")
        self.add_archer(other)
        return self  # Return the company instance to allow chaining

    def __iter__(self):
        # Make the class iterable by returning an iterator for the list of archers
        return iter(self.archers)

# Create Archer instances
Archer1 = Archer(1, 2, 3)
Archer2 = Archer(3, 4, 5)

# Create a Company with a maximum size of 4
company = Company(4)

# Add Archer2 to the company multiple times using the `+` operator
company = company + Archer2 + Archer2 + Archer2+ Archer1# Chaining additions

# Iterate through the company to print all the Archers
for archer in company:
    print(archer)
