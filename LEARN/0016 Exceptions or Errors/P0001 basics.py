# we use try except in python to catch any errors
try:
    # this is going to have error since a cannot be converted into an int
    a = int(input("Enter letter 'a': "))
except Exception as error:
    # create a method here what to do when an error occurs
    print('Invalid User Input - Error!', ': ' +
          str(error))  # now we have handled errors


# ------------------------------------
# We can also use specific exceptions
# ------------------------------------
try:
    # this is going to have error since a cannot be converted into an int
    print('opened')
    a = int(input("Enter letter 'a': "))
    print('closed')
except ValueError:
    print('Error: invalid user input')
except TypeError:
    print('Error: type error')
except KeyboardInterrupt:
    print('Error: keyboard interrupt')
finally:  
    # this is really important when your dealing with some data, but you got an error. you can add here a method to rectify anything if their is an error
    print('closed')
