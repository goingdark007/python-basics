# list comprehension

a = [1,2,3,4,5,6,7,8,9,10]

new = []

new = [i for i in a]
#copies every element of a
# first i is storing value
# mid is loop 

print(new)

new = [i for i in a if i%2==0]
# copies only even elements of a
# last is condition
# mid is loop
# first i is storing value

print(new)

new = [i*2 for i in a]
# stores the double of elements of a

print(new)