class A:
    def __init__(self):
        print('initialized a')

    def method1(self):
        print("method1")

    def method2(self):
        print("method2")


class B(A):  # inherit methods in class A
    def __init__(self):
        print('initialized b')

    def method3(self):
        print('method3')

    def method4(self):
        print('method4')


class C(B):
    def __init__(self):
        super().__init__()
        print('initialized c')

    def method5(self):
        print('method5')


a = A()
b = B()
c = C()

# a can only use method 1 and 2
a.method1()
a.method2()

# # b can only use method 1,2,3 and 4
b.method1()
b.method2()
b.method3()
b.method4()

c.method1()
c.method2()
c.method3()
c.method4()
c.method5()
