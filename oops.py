class student:
    def __init__(self, rollno, name, marks):
        self.rollno= rollno
        self.name= name
        self.marks= marks

    def print(self):
        print(self.rollno, self.name, self.marks)

# how to create an object
student1=student(1, "Satyam Singh", 30)
student1.print()