from dataclasses import dataclass
@dataclass
class bow:
    bow:str
    price:int
    damage:int

bow_a=bow('Lalsingh_bow',2,4)
print(bow_a)
bow_b=bow('Lalsingh_bow',2,4)
print(bow_b)
print(bow_a==bow_b)