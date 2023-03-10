# instead of using [ ] we are going to use () or using a constructor
# - You cannot reassign a value inside a tuple
tuple1 = (12, 13, 14, 15)
print(tuple1)
print(tuple1[0])  # 12

# ----------------------------------------
# you can convert a list to tuple
# ----------------------------------------
listItems = [1, 2, 3]
tuple2 = tuple(listItems)
print(tuple2)

# ----------------------------------------
# packing and unpacking
# - we cannot directly reassign value in a tuple but with packing and unpacking  we can
# ----------------------------------------
tuple3 = (1, 2, 3, 5)
l1 = list(tuple3)
l1[3] = 4
tuple3 = tuple(l1)
print(tuple3)
