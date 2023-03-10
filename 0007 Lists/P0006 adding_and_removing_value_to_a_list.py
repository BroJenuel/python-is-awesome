characters = ['a', 'b', 'c', 'd', 'e', 'f']

# we use <list>.append(<value>) to add value to the list
characters.append('g')
print(characters)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# we use <list>.remove(<value to remove>) to remove a value to the list
characters.remove('a')
print(characters)  # ['b', 'c', 'd', 'e', 'f', 'g']

# we use <list>.pop(<index>) to remove the item, this return the popped value
characters.pop(0)  # this will remove index 0 which is b
print(characters)  # ['c', 'd', 'e', 'f', 'g']
