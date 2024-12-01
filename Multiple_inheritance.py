import json
# Archer class
class Archer:
    def __init__(self, hp):
        self.hp = hp
    def walk(self):
        return "I am walking"
# JsonMixin class to serialize objects to JSON
class JsonMixin:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)
# SuperwalkMixin to add walking behavior
class superwalkmixin:
    def walk(self):
        return f"{super().walk()} extremely fast!"
# SuperArcher class inheriting from Archer, JsonMixin, and superwalkmixin
class superArcher(superwalkmixin,Archer, JsonMixin):
    pass
    # def __str__(self):
    #     return f"SuperArcher with {self.hp} HP and JSON: {self.toJSON()}"
# Creating an instance of superArcher
a = superArcher(100)
print(a.walk())# Walking behavior  # Calling walk() method from superwalkmixin
print(a.toJSON())
