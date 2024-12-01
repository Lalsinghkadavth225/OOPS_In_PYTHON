class A:
    def sayhi(self):
        print("Hello, i am from A")
class B(A):
    def sayhi(self):
        print("Hello, i am from B")
class C(B):
    def sayhi(self):
        print("Hello, i am from C")
class D(C,B):
    pass
d=D()
d.sayhi()
print(D.mro())


