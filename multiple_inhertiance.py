class A:
    def say_hi(self):
        print('Hello from A')
class B(A):
    def say_hi(self):
        print('Hello from B')
class C(B):
    def say_hi(self):
        print('Hello from C')
class D(A):
    # super.say_hi(self):
    pass
d=D()
d.say_hi()