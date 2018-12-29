students = []


class Student:

    school_name = "Springfield Elementary"

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


# Inheriting the behavior from the Student Class
class HighSchoolStudent(Student):

    school_name = "Springfield High School"  # Overriding the Class Attribute (school_name)

    def get_school_name(self):  # Overriding the get_school_name Method
        return "This is a High School Student"

    def get_name_capitalize(self):  # Overriding the get_name_capitalze Method
        original_value = super().get_name_capitalize()  # super(). = To define the Parent(Student) Class
        return original_value + "-HS"


james = HighSchoolStudent("james")
print(james.get_name_capitalize())

