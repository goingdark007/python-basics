# Stacks are Last In First Out, LIFO:
#| 4 |  ⬇️
#| 13 | ⬇️
#| 12 |
# They are stacked on top of each other. You can't access 12
# without popping 4 and 13.

stack = [] # List are basically stacks in python.

# push function
stack.append('A') # .append() is basically a push function in python.

stack.append('B')

stack.append('C')

print(stack) # C is the top element here.

stack.pop() # Pops top element which is C.

print(stack)

stack.pop() # Pops B cause now it's top element.

print(stack)

stack.append('B') # Bringing back B and C.

stack.append('C')

# peek function
print(stack[-1]) # negative index -1 prints the top or last element which is C.


# Queues are First In First Out, FIFO:
# REAR[ 65, 45, 35, 10] FRONT
#      ⬅️⬅️⬅️⬅️⬅️⬅️⬅️
# Think of it like a cash counter line where first element checks out and
# then the next element comes to check out. So, enque means get in line
# from the back in line and dequeue means getting out from the front the line.
# You can't access 45 without dequeue-ing 10 and 35.

from collections import deque # to import deque method.

queue = deque() # Creates an empty deque object called queue.

# enqueue
queue.append('Bob') # .append() method is enqueue-ing in queue.

queue.append('Mary')

queue.append('Joe')

print(queue)

queue.append('John') # Whoever comes in gets back of the line.

print(queue)

# dequeue
queue.popleft() # Basically pops the first element (Bob) in the line which is in left side.

print(queue)

# peek
print(queue[0]) # 0 index lets you peek or get the first element in the line