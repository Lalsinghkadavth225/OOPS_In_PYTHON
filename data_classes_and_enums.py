
class bow:
    def __init__(self,bow,cost,damage):
        self.cost=cost
        self.damage=damage
        self.bow=bow
bow_a=bow('Great_bow',3,54)
# print(bow_a.__dict__)
print(bow_a)
