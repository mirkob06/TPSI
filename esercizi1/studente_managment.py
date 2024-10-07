class Student():

    student_count = 0

    def __init__(self, name, age, student_number):
        self.name = name
        self.age = age
        self.student_number = student_number
        Student.student_count += 1

    def student_info(self):
        print (f"{self.name}, {self.age} years, {self.student_number}")

    @staticmethod
    def count():
        print (f"The number of student is: {Student.student_count}")

student1 = Student("Mario", 16, "2345")
student2 = Student("Maria", 13, "7654")    

print(student1)
print(student2)

student1.student_info()
student2.student_info()

Student.count()