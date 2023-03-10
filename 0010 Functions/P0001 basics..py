# -----------------------------------
# Basic way to use a function
# -----------------------------------
def myFunction():
    print("Hallo!")


myFunction()  # Hallo!

# -----------------------------------
# function by adding an argument
# -----------------------------------


def printName(name):
    print("Hallo! "+name)


printName("John")  # Hallo John


# -----------------------------------
# function with default parameter
# -----------------------------------
def printThis(message="This is just a message"):
    print(message)


printThis()  # This is just a message
printThis("Print this right here")  # Print this right here
