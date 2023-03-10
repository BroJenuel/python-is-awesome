try:
    a = int(input("one: "))
    b = int(input("two: "))

    print(a / b)
except ValueError:
    print('Invalid Input')
except ZeroDivisionError:
    print('Nothing can be divided by zero')
