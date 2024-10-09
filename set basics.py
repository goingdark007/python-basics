# set basics

s = set()

# it declares a variable as set

s.add(1)
s.add(2)
# .add() adds new elements
print(s,'\n')

s = {1,8,2,3}

s = s.union({ 8,11})
# .union() returns all the elements from both sets

print(s)

print()

s = {1,8,2,3}

s = s.intersection({ 8,11})
# . intersection() returns common elements from both sets

print(s)
