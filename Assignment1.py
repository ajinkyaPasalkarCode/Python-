'''
    Create an employee class as per the below requirement:
    Employee has name and id, it should be printable.
    Hint : name should be String, id should be int.
'''
class employee:
    def __init__(self, name, id):
        self.name=name
        self.id=id

    def display(self):
        print(f"name is {self.name} and His id are {self.id}") 

e1= employee('Aji',34)
e1.display()

class student:
    def __init__(self, studId, Stud_name):
        self.studId=studId,
        self.Stud_name=Stud_name
        
    def display(self):
        print(f"Student id are {self.studId} and student name is {self.Stud_name}")

s1=student(11,'Ajinkya pasalkar')
s1.display()        
              