class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + ' ' + last_name

    def show_full_name(self):
        self.full_name = self.

student1 = Student('Artem', 'Ludowell')
student2 = Student('Jack', 'Lukashik')
student3 = Student('Glib', 'Da')
students4 = Student()

print(student1.full_name)
print(student2.full_name)

student1.first_name = "Lox"
