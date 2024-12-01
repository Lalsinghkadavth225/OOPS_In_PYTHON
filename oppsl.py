
class student:
    def __init__(self, m1, s1):  # Corrected constructor name and parameter names
        self.m1 = m1
        self.s1 = s1

    def subject(self):
        print("subject is:", self.m1, self.s1)


# Creating instances of the student class with the correct parameters
cls = student('mat', 'science')
cls1 = student('math2', 'science11')

# Calling the subject method
cls.subject()  # Output: subject is: mat science
cls1.subject()  # Output: subject is: math2 science11
