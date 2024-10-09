print("hello world")
#This a single line comment 
""" This is a multiline 
comment"""
a = int(input("Enter the n begins: "))
b = int(input("Enter the n ends"))
for n in range (a,b+1):
    count = 0
    for i in range (1,n+1):
        for j in range (1,n+1):
            count += 1
        
    print (n,count)     