string = 'string'

# check if lower case
checker = string.islower()
print(checker)  # True

# check if upper case
checker = string.isupper()
print(checker)  # False

# change to upper
string = string.upper()
print(string)  # STRING

# change to lower case
string = string.lower()
print(string)  # string

# using swap case
string = "String"
string = string.swapcase()
print(string)  # sTRING


# check if digit
string = '29'
print(string.isdigit())  # True


# replace
string = '2 0 2 0 2'
string = string.replace('2', 'Hello')
print(string)  # Hello 0 Hello 0 Hello


# split
string = 'word1,word2,word3'
splittedString = string.split(",")  # returns a list
print(splittedString)  # ['word1', 'word2', 'word3']

# check if char is in string
string = 'sample'
print('e' in string)  # True
print('2' in string)  # False


# formatted string
name = 'John'
print(f"Hello! my name is {name}")  # Hello! my name is John
