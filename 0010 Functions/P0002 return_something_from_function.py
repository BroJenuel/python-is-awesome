# -----------------------------------
# basic return
# -----------------------------------
def reverse(string):
    return string[::-1]  # return anything only one time


reversedString = reverse("Hallo!")
print(reversedString)

# -----------------------------------
# once the return is done, it will not execute the next methods
# -----------------------------------


def reverse(string):
    return "here"
    return string[::-1]  # return anything only one time


reversedString = reverse("Hallo!")
print(reversedString)  # here
