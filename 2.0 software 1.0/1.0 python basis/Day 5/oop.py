class student:
    # self={
    

    # }
    def __init__(self, name, matricule, gpa, gender):
        # initialized the properties of this class
        self.name=name
        self.matricule=matricule
        self.gpa=gpa
        self.gender=gender
        # pass

    def take_lesson(self):
        return f"{self.name} is having matricule {self.matricule}"
    
    def semester_result(self):
        return f"{self.name} has a gpa of {self.gpa}"
    
    def student_gender(self):
        return f"{self.name} is a {self.gender}"
    
    def drop_lesson(self):
        return f"{self.name} is dropping Linear algebra"
# Imma start creating instances(Objects) of thus class student
first_student=student("Alen","Uba23PH127",3.4,"Female")
second_student=student("Emma","Uba23PH763", 2.9,"Male")
third_student=student("Safeh","Uba23PH233", 3.9,"Male")

print(f"FIRST STUDENT is: {first_student.name}")
print(f"Matricule: {first_student.matricule}")
print(f"Gpa: {first_student.gpa}")
print(f"Gender: {first_student.gender}")



print(f"SECOND STUDENT is: {second_student.name}")
print(f"Matricule: {second_student.matricule}")
print(f"Gpa: {second_student.gpa}")
print(f"Gender: {second_student.gender}")

print(f"Semester result: {first_student.semester_result}")