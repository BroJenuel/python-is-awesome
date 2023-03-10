# Class Employee
class Employee:  # this is a sample class for a employee
    def __init__(self, name, age, salary, gender, designation, department, responsibility, cpu, gpu, ram):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        self.email = self.generateEmail()
        self.job = self.Job(designation, department, responsibility)
        self.computer = self.Computer(cpu, gpu, ram)

    def generateEmail(self):
        return f'{self.name}@company.com'

    def showInfo(self):
        print(self.name, self.age, self.salary, self.gender, self.email)

    # Class JOB
    class Job:
        def __init__(self, designation, department, responsibility):
            self.designation = designation
            self.department = department
            self.responsibility = responsibility

        def showInfo(self):
            print(self.designation, self.department, self.responsibility)

    # Class Computer
    class Computer:
        def __init__(self, cpu, gpu, ram):
            self.cpu = cpu
            self.gpu = gpu
            self.ram = ram

        def showInfo(self):
            print(self.cpu, self.gpu, self.ram)


emp1 = Employee('John', 20, '$100,000', 'M', 'manager',
                'IT', 'Servers', 'i7', 'gtx 3060', '32GB')

emp1.showInfo()
emp1.job.showInfo()
emp1.computer.showInfo()
