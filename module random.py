# Module Random

import random
# imports random module

x = random.random()
# chooses radom float from 0 to 1

print(x)
# prints it

x = random.randint(1,5)
# chooses random integer from 1 to 5

print(x)
# prints it

list = [1,2,3,4,5]

random.shuffle(list)
# shuffle's the list and changes their sequence

print(list)
# prints it 

x = random.choice(list)
# chooses a random element from list

print(x)
# prints it 

x = random.choices(list,k = 3)
# chooses 3 random elements from list

print(x)
# prints as list