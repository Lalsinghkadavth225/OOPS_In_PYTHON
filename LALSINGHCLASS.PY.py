class Student:
    def __init__(self, name, roll_no, age):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.lap = self.Laptop()  # Create an instance of Laptop

    def show(self):
        print(self.name, self.roll_no, self.age)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'Hp'
            self.ram = 124
            self.cpu = 'I5'
        def show(self):
            print(self.brand,self.ram,self.cpu)


# Creating instances of the Student class
s1 = Student('lalsingh', 22, 24)
s2 = Student('madhi', 45, 23)

# Displaying the details of s1 and s2
s1.show()
s2.show()

# Accessing laptop instances for both students
lap1 = s1.lap
lap2 = s2.lap

