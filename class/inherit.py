class student:
    def __init__(self,name,avg,percentage):
        self.name=name
        self.avg=avg
        self.percentage=percentage
    def average(self):
        return sum(self.marks)/len(self.marks)
