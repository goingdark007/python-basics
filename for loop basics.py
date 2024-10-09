# for loop basics

for i in range(5):
    print(i)   
# by default starts from 0 ends 5-1 = 4

for i in range(1,20,2):
    print(i)
# ,2) is a step that skips i value by 1     

a = 'hello world'

for i in a:
    print(i,end=' ')
# prints every element of a
# i stores every element of a at a time

print()

for i in range (1,20):
    if i%2==0:
        continue
    print(i)
# skips iteration and does not send i value
# to code if the condition is true

for i in range (1,11):
    if i==5:
        break
    print(i)
# stops the loop and throws the i value outside 