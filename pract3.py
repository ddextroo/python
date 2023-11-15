class Employee:
    def __init__(self, name= None, salary = None):
        self.__name = name
        self.__salary = salary
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name 
        
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, salary):
        self.__salary = salary
    
    def calculate_salary(self):
        return self.__salary
class Manager(Employee):
    def __init__(self, name, salary, bonus=None):
        super().__init__(name,salary)
        self.__bonus = bonus
        
    def calculate_salary(self):
        return super().salary + (super().salary * self.__bonus)
    
class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.__bonus = 0.10
        
    def calculate_salary(self):
        return super().salary + (super().salary * self.__bonus)
    
class Designer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.__bonus = 0.08
        
    def calculate_salary(self):
        return super().salary + (super().salary * self.__bonus)
    
manager = Manager("dexter", 30000, 20)
developer = Developer("hehe", 8000)
designer = Designer("haha", 5000)

employees = [manager, developer, designer]
for employee in employees:
    print(employee.calculate_salary())     