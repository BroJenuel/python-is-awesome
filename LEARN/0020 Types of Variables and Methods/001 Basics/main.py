class Employee:  # this is a sample class for a employee
    # this are class variables
    company = 'learn2code'

    def __init__(self, name, age, salary, gender):
        # this are instance variables
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        self.email = self.generateEmail(Employee)

    def generateEmail(self, cls):
        return f'{self.name}@{cls.company}.com'

    def showInfo(self):
        print(self.name, self.age, self.salary, self.gender, self.email)

    @classmethod
    def changeCompanyName(cls, newName):
        cls.company = newName

    @staticmethod
    def info():
        print('This is a class for creating Object, it required parameter which are name, age, salary and gender')


Employee.changeCompanyName('learnToCode')

emp1 = Employee('John', 20, '$100,000', 'M')
emp1.info()
emp1.showInfo()
