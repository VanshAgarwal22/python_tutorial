#class and object

class employee:
    def __init__(self,name,salary):  #constructor
        self.name =name
        self.salary = salary        
    
    def getsalary(self):
        print(self.salary)


rohan= employee("rohan", "34565")
print(rohan.salary)
print(rohan.name)

vansh = employee("vansh", "1234567")
vansh.getsalary()