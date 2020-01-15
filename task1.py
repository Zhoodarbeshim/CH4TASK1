class Student():
    def __init__(self, name, last_name, year_of_entrance, department):
        self.name = name
        self.last_name = last_name
        self.department = department
        self.year_of_entrance = year_of_entrance
    
    def get_student_info(self):
        return f"{self.name} {self.last_name} поступил в {self.year_of_entrance} году на факультет {self.department}."

student = Student('Вася', 'Иванов', '2017', '"Программирование"')
print(student.get_student_info())