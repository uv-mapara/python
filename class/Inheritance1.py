class student:
    def __init__(self,name,school,mark):
        self.name=name
        self.school=school
        self.marks=mark
    def average(self):
        return sum(self.marks)/len(self.marks)

class WorkingStudent(student):
    def __init__(self,name,school,mark,salary):
        super().__init__(name,school,mark)
        self.salary=salary   
    def func2(self):
        avg=super().average()
        return avg
    def weeklysalary(self):
        return self.salary*7
obj=student("vivek","Oxford",[76,89,94,39,98])
print(obj.average())

obj1=WorkingStudent("yash","Mit",[67,89,90,80,78],100)
print(obj1.func2())
print(obj1.average())
print(obj1.weeklysalary())