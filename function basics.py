# function basics

#def function(parametes):
#    code
#function
# syntax and function calling runs code

def sum():
    print(5+6)
sum()
# def defines the sum as function
# when called prints 11

def sum(a,b):
    return a+b
a = sum(10,20)
print(a)  
b= sum(5,7) 
print(b)
# returns value and stores them
# 20 and 10 is parameters


def math(a,b):
    return a+b,a-b
a = math(20,10)
b,c = math(20,10)
print(a,b,c) 
# returns multiple values unlike C
# if stored in one variable stores as tuple
# if stored in multiple variables stores as
# individually

#if _name_ == '_main_':
#    main()
#def main():   
# is used to create main function like C

def greet(name='stranger'):
    print(name)
greet() 
greet('nazmul')  
# arguement is like default if not 
# parameter is assigned then prints
# otherwise prints the assigned