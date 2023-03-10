student = {
    'name': 'John Mark',
    'age': 17,
    'allowance': 1600.00,
    'major': 'Information Technology'
}

print(student['name'], student['allowance'])


# how to loop through it
for i in student:
    print(i)

for i in student.keys():
    print(i)

for i in student.values():
    print(i)

# print in a neat order
for key in student:
    print(key+": " + str(student[key]))
