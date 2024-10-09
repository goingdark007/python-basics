#while loop basics

a = 1

while a <= 10:
    print(a)
    a += 1
# starting point is written outside
# condition in side and incrementation
# in body

a = 0

while a <= 10 :
    a += 1
    if a < 6:
        continue
    print(a)
# continue skips the iterations
# just like step, does not send value to code
print()a = 1

while a <= 10:
    if a == 6:
        break 
    print(a)
    a += 1
print(a) 

a = 1

while a <= 10:
    if a == 6:
        break 
    print(a)
    a += 1
print(a)    
# break stops the loop at 6 and throws it 
# outside the loop      