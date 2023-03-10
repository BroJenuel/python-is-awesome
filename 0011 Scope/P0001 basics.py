
# -----------------------------------
# local and global variable
# -----------------------------------

x = 20  # exists on global

# this will not be able to change x because because x inside the changeX is a local and cannot reach the global


def changeX():
    x = 10


changeX()
print(x) # 20


# the only way to change is to set x global inside the function to get access to the global variable
def changeX():
    global x
    x = 10


changeX()
print(x) # 10
