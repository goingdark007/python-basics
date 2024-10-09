#recursion basics
#syntax:-

# def recusion():
    #return recursion()

def factorial(n):
    if n == 1:
        return n
    else:
        return  n* factorial(n-1)

num = 6

print(factorial(num))
# if condition false recalls the function and
# returns value

def fibonacci(n):
    if n<= 1:
        return n
    else:
        return(fibonacci(n-1)+ fibonacci(n-2))

for i in range (10):
    print(fibonacci(i))  
# prints fibonacci recursively