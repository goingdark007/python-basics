# module time

import time

t = time.localtime(time.time())
# gets the current time as structure
# time.time() gets time as seconds

n = time.asctime(t)
# .asctime(t) concerts the structure into a
# printable format.

print(n)
# prints it

m = '13:40:20'

n = time.strptime(m,'%H:%M:%S')
# it converts string into a time structure

p = time.asctime(n)
# converts structure into printable format

print(p)
#prints it


i = 10
# declares and assigns value

while i >= 0:
    
    print(i)
    i -= 1
    #decrements
    time.sleep(1)
    # it gives 1 second interval between each print
