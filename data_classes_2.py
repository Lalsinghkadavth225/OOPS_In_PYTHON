from dataclasses import dataclass
@dataclass(frozen=True,order=True)
class bow:
    bow:str
    rate:int
    loss:int
bow_a=('bow',2,4)
bow_b=('zow',2,4)
print(bow_a>bow_b)