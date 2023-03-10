# note run your terminal in this directory

with open('files/data.txt', 'r') as file:
    data = file.read()
    print(data)

with open('files/data.txt', 'r') as file:
    data = file.readline(4)
    print(data)

with open('files/data.txt', 'r') as file:
    data = file.readlines()
    print(data)
