class Employee:  # this is a sample class for a employee
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        self.email = self.generateEmail(Employee)

    def generateEmail(self):
        return f'{self.name}@company.com'

    def showInfo(self):
        print(self.name, self.age, self.salary, self.gender, self.email)


emp1 = Employee('John', 20, '$100,000', 'M')
emp1.showInfo()
