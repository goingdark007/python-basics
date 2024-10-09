# List basics

l = [1,7,'nazmul']

print(l[0])
# prints element at 0 index

print(l[2])
# prints element at 2 index

l = [1,8,7,2,21,15]

l.sort()
# sorts the elements in ascending order
print(l)

l.reverse()
# reverses the elements from ascending to descending

print(l)

l = [1, 2, 7, 8, 15, 21]

l.append(8)
# adds 8 at end of the list

print(l)

l = [1, 2, 7, 8, 15, 21]

l.insert(3,8)
# inserts element 8 at 3 index and moves
# present element by storing it to index 4

print(l)

l = [1, 2, 7, 8, 15, 21]

n = l.pop(2)
# pops the element stored at 2 index and 
# stores it value to another variable

print(l,'\t',n)

l = [1, 2, 7, 8, 15, 21]

l.remove(21)
# removes element 21 from list

print(l)

l = [1,1,2,5]

n = l.count(1)
# counts a element is repeating how many times

print(n)

n = l.index(5)
# finds the index of element 5

print(n)